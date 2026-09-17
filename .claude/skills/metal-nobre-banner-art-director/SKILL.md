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

When available, use the UI/UX Pro Max `banner-design` skill as the general banner-design method. This skill adds only the Metal Nobre-specific decisions.

## Core Principle

**Plan here. Render elsewhere.**

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
- 1 optional additional product;
- official logo separately.

For each product, state its role explicitly.

Example:
- Image 1 = hero faucet
- Image 2 = basin paired with hero faucet
- Image 3 = shower in secondary zone
- Image 4 = toilet in secondary zone
- Image 5 = official logo

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

## Anti-Patterns

Do not:
- attach a prior generated banner as a default visual reference;
- force every brand into the same bathroom/room;
- make the skill a repository of historical experiments;
- carry superseded dimensions or old prompts;
- ask the image model to decide the product mix;
- ask the image model to recreate the logo when the real asset is available;
- overload the prompt with internal process language.

## Success Criterion

The planner should produce a brief that is short enough to use directly in an image session, but specific enough that the generator is not deciding the brand story on its own.
