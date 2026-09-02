# Evidence Index — JET / Metal Nobre

## Purpose

This index records **what each validated visual artifact can legitimately prove**.

The original training videos and transcript files remain primary source material. The extracted Pack A clips/screenshots are targeted evidence, not replacements for the original sources.

Binary media is not embedded in this Markdown file. Stable `VIS` IDs, source module, timestamp and expected filenames provide the linkage layer.

## Evidence status

- `VERIFIED` — inspected against transcript; supports intended visual claim.
- `INSUFFICIENT` — valid capture but does not prove the intended final state.
- `METADATA_CORRECTION` — asset remains valid; description/boundary corrected without recapture.

## Pack A index

| Visual ID | Source window | Asset(s) | Status | What it proves | Supports / caveat |
|---|---|---|---|---|---|
| `MOD1-VIS-001` | MOD1 `00:09:00–00:10:45` | `MOD1_VIS_001_00h09m00s-00h10m45s.mp4` | `VERIFIED` | `Novo Usuário`, user form, `Áreas de Acesso`, modules/tools and access toggles. | `JET-KB-004`, `PEN-033` |
| `MOD1-VIS-002` | MOD1 `00:13:06–00:14:21` | `MOD1_VIS_002_00h13m06s-00h14m21s.mp4` | `VERIFIED` | Sensitive admin permissions for anonymization, order-status operations and monetary/dashboard access. | `JET-KB-005`; does not validate legal interpretation. |
| `MOD1-VIS-003` | MOD1 `00:21:53–00:24:10` | `MOD1_VIS_003_00h21m53s-00h24m10s.mp4` | `VERIFIED` | Sender list/create surface and default-sender control. | `JET-KB-049`, `PEN-014` |
| `MOD1-VIS-004` | MOD1 `00:30:47–00:32:09` | `MOD1_VIS_004_REVIEW_BEFORE_UPLOAD_00h30m47s-00h32m09s.mp4` | `VERIFIED` | Integration scope/queue surface, queue statuses and technical actions. | `JET-KB-064`–`066`, `JET-RULE-004`. Credential values themselves are not canonical knowledge. |
| `MOD1-VIS-005` | MOD1 `00:34:12–00:39:29` | `MOD1_VIS_005_A_00h34m20s.png`; `B_00h35m30s.png`; `C_00h37m20s.png`; `D_00h38m05s.png`; `E_00h38m55s.png` | `VERIFIED` + `METADATA_CORRECTION` | Storewide parametrization surface, listing/detail sold-out behavior, zero-value examples, discount-basis control and awaited-product e-mail flag. | `JET-KB-041`, `JET-KB-051`. B/C notes corrected below. |
| `MOD2-VIS-001` | MOD2 `00:02:01–00:06:16` | `MOD2_VIS_001_00h02m01s-00h06m16s.mp4` | `VERIFIED` | Category tree/nesting, product counts, actions and URL/SEO edit surface. | `JET-KB-007`–`010`. UI editability alone does not prove authority. |
| `MOD2-VIS-002` | MOD2 `00:22:53–00:26:04` | `MOD2_VIS_002_00h22m53s-00h26m04s.mp4` | `VERIFIED` | Drag/drop category reordering across hierarchical positions. | `JET-KB-011`, `JET-RULE-003` |
| `MOD2-VIS-003` | MOD2 `00:51:07–00:55:40` | `MOD2_VIS_003_A_00h51m15s.png`; `B_00h52m55s.png`; `C_00h54m20s.png`; `D_00h55m20s.png` | `VERIFIED` | Product `Dados principais`, stock/price/category, package dimensions and cross-docking field surface. | `JET-KB-013`–`018`; source-of-truth comes from transcript/integration evidence. |
| `MOD2-VIS-004` | MOD2 `00:55:40–00:59:02` | `MOD2_VIS_004_00h55m40s-00h59m02s.mp4` | `VERIFIED` | Main vs alternative image behavior and multifoto configuration/presentation. | `JET-KB-019`, `JET-KB-020`, `PEN-008` |
| `MOD2-VIS-005` | MOD2 `01:03:00–01:06:18` | `MOD2_VIS_005_A_01h03m05s.png`; `B_01h04m06s.png`; `C_01h05m05s.png`; `D_01h05m55s.png` | `INSUFFICIENT` for final-state proof | Product/store sold-out and stock-control surfaces are visible. Frame B captures automatic sold-out flag as `Não` immediately before the spoken instruction to change it to `Sim`. | `JET-KB-043`. Do **not** cite B as final-state `Sim`; verify current live setting in `PEN-018`. |
| `MOD2-VIS-006` | MOD2 `01:15:27–01:20:00` | `MOD2_VIS_006_01h15m27s-01h20m00s.mp4` | `VERIFIED` | Import-products flow, tutorial/model spreadsheet and strict bulk-update structure. | `JET-KB-032`, `JET-RULE-006` |
| `MOD2-VIS-007A` | MOD2 `01:29:30–01:31:20` | `MOD2_VIS_007A_01h29m30s-01h31m20s.mp4` | `VERIFIED` + `METADATA_CORRECTION` | `Atributo Único` / meter-per-box value-management portion. | `JET-KB-037`, `JET-KB-038`. Product linking starts in 007B. |
| `MOD2-VIS-007B` | MOD2 `01:31:01–01:34:19` | `MOD2_VIS_007B_01h31m01s-01h34m19s.mp4` | `VERIFIED` + `METADATA_CORRECTION` | Product linking followed by storefront m²/box calculator, rounding and cart behavior. | `JET-KB-039`; does not prove Sankhya return conversion (`JET-KB-040`). |
| `MOD2-VIS-008` | MOD2 `01:34:56–01:40:47` | `MOD2_VIS_008_01h34m56s-01h40m47s.mp4` | `VERIFIED` | Product Similar setup, name/code, product selection, palette/image/text modes and storefront switching. | `JET-KB-025`–`027`, `PEN-012` |
| `MOD2-VIS-009` | MOD2 `01:40:48–01:44:19` | `MOD2_VIS_009_01h40m48s-01h44m19s.mp4` | `VERIFIED` | Product-group IDs, editing/linking/new-group behavior and storefront presentation. | `JET-KB-030`, `JET-KB-031`, `JET-RULE-005` |
| `MOD2-VIS-010` | MOD2 `01:45:19–01:49:05` | `MOD2_VIS_010_01h45m19s-01h49m05s.mp4` | `VERIFIED` | 404 before detail-page change → accessible detail afterward → `Esgotado`/`Avise-me` → Produtos Aguardados/report flow. | Strong support for `JET-KB-042`, `044`–`046`; `MN-DEC-005/006`. |

## Metadata corrections

### `MOD1-VIS-005`

Use these normalized descriptions:

- `A @ 00:34:20` — store parametrization/listing sold-out context;
- `B @ 00:35:30` — category/listing view with product cards, including zero-value examples;
- `C @ 00:37:20` — sold-out product-detail state showing `Esgotado` / `Avise-me`;
- `D @ 00:38:05` — discount-basis control context;
- `E @ 00:38:55` — automatic awaited-product e-mail control context.

Do not retain the original B/C notes that swapped the intended topics.

### `MOD2-VIS-007A/B`

Normalize the boundary as:

- `007A` — create/manage the Atributo Único meter-per-box value;
- `007B` — link product to the value, then observe calculator/cart behavior.

## Evidence that must remain non-visual or externally verified

Old training visuals must **not** be used to resolve:

- legal/LGPD correctness;
- sitemap 12h/24h refresh cadence;
- current automatic state of `Quem comprou, comprou também`;
- current state of features described as being discontinued;
- whether Atributo Único integration from Sankhya is implemented;
- whether m²/box return conversion is implemented;
- final freight architecture;
- final payment architecture;
- current support handoff state.

## Provenance rule for future IT/PO/agents

When a future document or agent rule relies on visual evidence, store both:

```yaml
visual_id: MOD2-VIS-010
source_module: MOD2
timestamp_start: "01:45:19"
timestamp_end: "01:49:05"
validation_status: VERIFIED
supports:
  - JET-KB-042
  - JET-KB-044
  - JET-KB-045
  - JET-KB-046
ui_context: training-time interface
```

Never cite the existence of a screenshot/clip as proof of something that is only spoken, inferred or time-sensitive.

## Estado do material bruto de treinamento — 02/09/2026

Material em `Videos/Treinamento_Ecommerce/` (fora deste repo: 3,2 GB de vídeo e
áudio, e contém tela de painel com dados sensíveis).

| Módulo | Vídeo | Transcrito | Pacote A (evidência visual) | Canônico derivado |
|---|---|---|---|---|
| MOD1 | sim | `Transcripto MOD1.txt` | 4 clipes + 5 frames | `knowledge-base.md` |
| MOD2 | sim | `Transcripto MOD2.txt` | 9 clipes + 8 frames | `knowledge-base.md` |
| MOD3 | **não existe** — Fabrício entregou lista de 20 tutoriais (`video/MOD3/MOD3.txt`) | n/a | n/a | `campanhas-busca-venda-assistida.md` |
| MOD4 | sim (66 min, 28/08) | `AUDIO_COMPLETO_MOD4.{txt,srt,vtt,tsv,json}` — Whisper local, 02/09 | **pendente** | `frete-e-pagamento-mod4.md` |

Manifesto do Pacote A: `evidence/manifest_pack_a.csv`, 26 visuais com
`visual_id`, timestamp de início/fim e caminho do arquivo. `MOD1-VIS-004` está
marcado como sensível (escopo e filas) e exige revisão antes de qualquer upload
externo.

### Como transcrever um módulo novo

`ffmpeg` e `whisper` estão instalados na máquina do Leandro — não é preciso
passar por serviço externo, e o áudio não sai da máquina:

```bash
ffmpeg -y -i "video/MODn/<arquivo>.mp4" -vn -ac 1 -ar 16000 -c:a libmp3lame -q:a 5 "audio/AUDIO_COMPLETO_MODn.mp3"
PYTHONIOENCODING=utf-8 whisper "audio/AUDIO_COMPLETO_MODn.mp3" --model small --language pt --output_format all --output_dir resultados --fp16 False
```

Roda em CPU a cerca de 0,75x do tempo real (66 min de áudio levaram 48 min).
O `.tsv` e o `.json` carregam timestamps por segmento — é por eles que se
recorta o Pacote A depois.

Transcrição automática erra nome próprio: "frenete" (Frenet), "Sunker"
(Sankhya), "Pixie" (PIX), "GDLog" (Jadlog). Sentido se reconstrói; **número
crítico se reconfere na tela**.
