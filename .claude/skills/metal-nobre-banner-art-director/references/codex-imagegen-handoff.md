# Codex image-generation handoff

Use one separate Codex task per brand to keep image generations and revisions out of the director task. The director task owns product selection, brief, prompt and approval gates. Create the generator task only after the brief/prompt is approved and the official product images are verified.

## Handoff packet

Send the generator task only the approved prompt and these execution inputs:

- brand and final banner purpose;
- current repository `TASK.md` revision or approved brief version;
- local file path for each official product image, indexed with its exact SKU and visual role;
- final export size and the area that must survive cropping;
- output directory and versioned filename convention;
- fixed constraints: required products, no substitutes/duplicates, no logo or text;
- QA and the gate at which the generator must stop.

Do not send historical ZIPs, generated banners or superseded prompts as default references. The generator should read the packet, not infer a new strategy from the director conversation.

## Built-in generation and crop

Use Codex's built-in image-generation tool by default. It can take local product images as direct references. Its call does not expose an exact output-size parameter; measure the resulting file. Copy the selected generation from Codex's generated-images storage into the project workspace before treating it as an asset. Keep candidates and revisions under distinct versioned filenames.

The documented GPT Image generation limit is a 3:1 long-to-short ratio. When the JET export target is wider, ask for a landscape composition with a crop-safe horizontal band. Scale the chosen source proportionally to the target width, then crop a preview to the **final target dimensions** before D2. Never stretch it. Check whether the source has enough resolution for this step. Approve or reject the scene based on both the source and that preview. If required products are cut, distorted, missing or visually too small in the crop, revise the composition or revisit the target height.

The generator returns the source file path, measured dimensions, crop-preview path and a concise QA finding. It stops at D2. Logo, headline, supporting copy, final compression and JET upload belong to later gates.

The built-in tool is the normal Codex path and needs no API key. Use an API/CLI fallback only after the user explicitly chooses it. See the current [Codex image-generation guidance](https://learn.chatgpt.com/docs/image-generation) and [image API size limits](https://developers.openai.com/api/docs/guides/image-generation) before relying on tool capabilities that can change.
