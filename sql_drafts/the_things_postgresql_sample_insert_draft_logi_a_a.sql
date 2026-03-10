UPDATE documents
SET content_body = $fwos$
# fwos baseline (unified)

## purpose

This document defines the operational baseline of fwos.

It establishes:

* semantic document structure
* keyword interpretation rules
* collaboration roles
* external identification rules
* original text preservation rules

This baseline governs how fwos documents are created, interpreted, and stored.

---

## field model

fwos operates as a truss field connecting:

AI (logi / moa / grigo)  
Human (SeungeFlow)  
Database (PostgreSQL)

Roles:

* Human maintains coherence and observation  
* AI organizes structure and derives relations  
* DB preserves immutable past states  

---

## internal baseline (semantic layer)

### document completeness rule

fwos documents must be semantically complete without requiring file names or tags.

Meaning must exist entirely inside the document.

---

### original_text_rule

If a document contains original Korean statements,
they must be preserved exactly as written.

Original Korean text must never be paraphrased,
translated in place, or structurally altered.

Translations or interpretations must be placed separately.

This rule ensures that observation records remain intact
while allowing structural interpretation layers to evolve.

---

### snapshot structure

fwos documents may include:

* meta_summary_ko  
* purpose  
* root_summary  
* core_definition  
* role_model  
* status  

Additional domain sections are allowed and treated as artifacts.

---

### keyword generation rule

Keywords are not written into documents.

Keywords are derived by AI after document creation.

They represent structural coordinates, not classification tags.

Rules:

* choose minimal structural words  
* prefer 1–3 keywords  
* wide keywords are acceptable  
* overlap indicates structural convergence  

Keywords exist only in the linkage layer, not in author text.

---

## external baseline (identity layer)

### external_identifier_rule

fwos documents use external identifiers independent of meaning.

File names consist of:

* AI prefix (logi / moa / grigo)  
* UUID identifier  

Format example:

logi_4f3c8b2e-8c4a-4e2a-a3b7-21f4b0f2c9a1.md  

File names carry no semantic meaning.  
They serve only as storage addresses.

Meaning exists only inside the document.

---

## collaboration baseline

logi (chatgpt) is the primary structural interpreter.

Other AI systems may provide supporting materials,
but they do not define fwos structural rules.

Human defines direction and observation.  
AI derives structure.  
DB preserves states.  

---

## baseline principle

fwos baseline is not a stored object name.

It is a rule system governing document generation,
interpretation, and storage.

This document itself may be stored as a reference anchor
within the database.

---

end.
$fwos$
WHERE document_name = 'fwos_baseline_unified';
