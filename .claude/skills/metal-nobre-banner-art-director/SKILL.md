---
name: metal-nobre-banner-art-director
description: Use when planning a manufacturer-page banner for the Metal Nobre e-commerce before sending the visual brief and product references to an image-generation session.
---

# Metal Nobre Banner Art Director

## Purpose

Plan premium manufacturer-page banners for Metal Nobre.

This skill does **not** render the final image.

Its job is to transform:
- brand;
- product selection;
- official product references;
- commercial goal;
- JET constraints;

into a concise, production-ready **Image Generation Brief**.

When available, use UI/UX Pro Max `banner-design` for relevant art direction, visual hierarchy, safe areas and legibility. The Metal Nobre deliverable is a static image; generic HTML/CSS, CTA and size presets do not override the current `TASK.md`.

## Core Principle

**Plan in the director task. Render in a separate task for each brand.**

In Codex, read [references/codex-imagegen-handoff.md](references/codex-imagegen-handoff.md) when preparing the generator handoff. Do not send a candidate prompt to generation before its explicit approval gate and verified product references.

Do not carry old generated banners forward as visual references unless the user explicitly asks to replicate one.

Preserve the **quality bar and design principles**, not the literal room, composition, furniture, or camera angle of a previous banner.

## Standard Workflow

1. Understand the manufacturer and category.
2. Select the visual story.
3. Select the real products that should appear.
4. Resolve/verify official product references.
5. Define product hierarchy.
6. Define art direction.
7. Define copy.
8. Define layout.
9. Produce a short generation prompt.
10. Produce a QA checklist.

## Product Reference Rule

For production banners, prefer direct image references supplied to the image-generation session.

Do not rely on:
- a ZIP to indirectly expose images;
- model memory of the product;
- vague product-category descriptions when fidelity matters.

Recommended reference package:
- 1 hero product;
- 1 main supporting product;
- 1 secondary supporting product;
- 1 optional additional product.

Keep the official logo outside the generator reference package when it will be applied in post-production.

For each product, state its role explicitly.

Example:
- Image 1 = hero faucet
- Image 2 = basin paired with hero faucet
- Image 3 = shower in secondary zone
- Image 4 = toilet in secondary zone

## Banner System

The system must feel consistent across brands through:
- premium visual quality;
- restrained typography;
- generous but efficient whitespace;
- architectural/editorial art direction;
- strong product hierarchy;
- controlled copy density.

Do **not** make every manufacturer look like Deca.

The scene and art direction must adapt to the category.

## Category Directions

### Metals / sanitaryware / kitchen
Architecture + real products.
Examples: Deca, Docol, Roca, DAX, Doka, Franke, Tramontina.

### Surfaces / coverings
Architecture + materiality.
Examples: Decortiles, Eliane, Castelatto, Galleria Biancogres.

### Wood
Interior + grain + warmth.
Example: Indusparquet.

### Wellness
Water + atmosphere + relaxation.
Example: Jacuzzi.

### Accessories / hardware
Sculptural product detail + refined interior context.
Examples: Zen Design, Italy Line, Pasinato, Nina Martinelli.

## Branding Rule

Recommended production flow:

1. Generate **environment + products**.
2. Add the official manufacturer logo and text **deterministically afterward**.

Do not ask the image model to recreate an official logo when the asset already exists.

## Output Contract

The planner must return exactly these sections:

### 1. IMAGE GENERATION BRIEF
- brand
- category
- purpose
- target aspect/size
- final crop target versus feasible generation framing
- product story
- product hierarchy
- environment
- palette/materials
- lighting
- layout
- copy
- branding instructions

### 2. REFERENCE MAP
Map each image to its role.

### 3. GENERATION PROMPT
Keep it concise and specific.
Prefer clear scene direction over a long rule list.

### 4. POST-PRODUCTION SPEC
- official logo
- headline
- supporting copy
- approximate placement
- export format/size
- compression requirement

### 5. QA CHECKLIST
Check:
- product fidelity
- required-product visibility
- composition
- brand distinctiveness
- logo fidelity
- text correctness
- JET output constraints
- final-crop visibility and safe areas

## Anti-Patterns

Do not:
- attach a prior generated banner as a default visual reference;
- force every brand into the same bathroom/room;
- make the skill a repository of historical experiments;
- carry superseded dimensions or old prompts;
- ask the image model to decide the product mix;
- ask the image model to recreate the logo when the real asset is available;
- assume that the generated image has the JET's exact final dimensions;
- overload the prompt with internal process language.

## Reference routing

- [references/art-direction.md](references/art-direction.md): read when choosing a category's visual language.
- [references/jet-spec.md](references/jet-spec.md): read when setting a production export target.
- [references/planner-output-template.md](references/planner-output-template.md): read when the output needs the standard five-section format.
- [references/codex-imagegen-handoff.md](references/codex-imagegen-handoff.md): read when dispatching a Codex generator task.

## Success Criterion

The planner should produce a brief that is short enough to use directly in an image session, but specific enough that the generator is not deciding the brand story on its own.
