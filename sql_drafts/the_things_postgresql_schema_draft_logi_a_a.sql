BEGIN;

CREATE TABLE IF NOT EXISTS documents (
    document_id BIGSERIAL PRIMARY KEY,
    document_name TEXT NOT NULL UNIQUE,
    document_title TEXT,
    document_class TEXT NOT NULL,
    primary_role TEXT NOT NULL,
    related_object TEXT NOT NULL,
    source_origin TEXT NOT NULL,
    current_status TEXT NOT NULL,
    content_body TEXT NOT NULL,
    content_format TEXT,
    original_text_required TEXT NOT NULL DEFAULT 'yes',
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ
);

ALTER TABLE documents
    DROP CONSTRAINT IF EXISTS documents_original_text_required_chk;

ALTER TABLE documents
    ADD CONSTRAINT documents_original_text_required_chk
    CHECK (original_text_required IN ('yes', 'no', 'partial'));

CREATE TABLE IF NOT EXISTS document_lineage (
    lineage_id BIGSERIAL PRIMARY KEY,
    lineage_group TEXT NOT NULL,
    document_id BIGINT NOT NULL,
    lineage_position TEXT NOT NULL,
    previous_document_id BIGINT,
    next_document_id BIGINT,
    lineage_order INTEGER,
    lineage_note TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT document_lineage_document_fk
        FOREIGN KEY (document_id)
        REFERENCES documents (document_id)
        ON DELETE CASCADE,

    CONSTRAINT document_lineage_previous_document_fk
        FOREIGN KEY (previous_document_id)
        REFERENCES documents (document_id)
        ON DELETE SET NULL,

    CONSTRAINT document_lineage_next_document_fk
        FOREIGN KEY (next_document_id)
        REFERENCES documents (document_id)
        ON DELETE SET NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_document_lineage_group_position
    ON document_lineage (lineage_group, lineage_position);

CREATE UNIQUE INDEX IF NOT EXISTS uq_document_lineage_group_document
    ON document_lineage (lineage_group, document_id);

CREATE TABLE IF NOT EXISTS document_layers (
    layer_id BIGSERIAL PRIMARY KEY,
    document_id BIGINT NOT NULL,
    layer_type TEXT NOT NULL,
    language_code TEXT,
    layer_content TEXT NOT NULL,
    preservation_required BOOLEAN NOT NULL DEFAULT TRUE,
    layer_order INTEGER,
    source_note TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT document_layers_document_fk
        FOREIGN KEY (document_id)
        REFERENCES documents (document_id)
        ON DELETE CASCADE,

    CONSTRAINT document_layers_layer_type_chk
        CHECK (layer_type IN ('original', 'translation', 'interpretation', 'summary'))
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_document_layers_doc_type_lang_order
    ON document_layers (document_id, layer_type, COALESCE(language_code, ''), COALESCE(layer_order, 0));

CREATE TABLE IF NOT EXISTS ingest_records (
    ingest_id BIGSERIAL PRIMARY KEY,
    document_id BIGINT NOT NULL,
    ingest_stage TEXT NOT NULL,
    ingest_priority_group TEXT,
    ingest_reason TEXT,
    ingest_source_window TEXT,
    ingest_note TEXT,
    ingested_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT ingest_records_document_fk
        FOREIGN KEY (document_id)
        REFERENCES documents (document_id)
        ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_documents_document_name
    ON documents (document_name);

CREATE INDEX IF NOT EXISTS idx_documents_document_class
    ON documents (document_class);

CREATE INDEX IF NOT EXISTS idx_documents_related_object
    ON documents (related_object);

CREATE INDEX IF NOT EXISTS idx_document_lineage_group
    ON document_lineage (lineage_group);

CREATE INDEX IF NOT EXISTS idx_document_lineage_document_id
    ON document_lineage (document_id);

CREATE INDEX IF NOT EXISTS idx_document_layers_document_id
    ON document_layers (document_id);

CREATE INDEX IF NOT EXISTS idx_document_layers_layer_type
    ON document_layers (layer_type);

CREATE INDEX IF NOT EXISTS idx_ingest_records_document_id
    ON ingest_records (document_id);

CREATE INDEX IF NOT EXISTS idx_ingest_records_stage
    ON ingest_records (ingest_stage);

CREATE OR REPLACE FUNCTION set_documents_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_set_documents_updated_at ON documents;

CREATE TRIGGER trg_set_documents_updated_at
BEFORE UPDATE ON documents
FOR EACH ROW
EXECUTE FUNCTION set_documents_updated_at();

COMMIT;
