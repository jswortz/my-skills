---
name: gcp-diagram
description: Generate professional GCP-branded architecture diagrams using Gemini image generation models. Use when the user asks to create architecture diagrams, system diagrams, data flow diagrams, deployment diagrams, database schema diagrams, or any technical diagram styled like official Google Cloud Platform documentation. Also use when asked to visualize GCP architectures, agent systems, microservices, or service topologies. Supports gemini-3-pro-image-preview and gemini-2.5-flash-image models via Vertex AI.
---

# GCP Architecture Diagram Generator

Generate publication-quality architecture diagrams styled like official Google Cloud Platform documentation using Gemini image generation.

## Workflow

### 1. Gather Architecture Details

From user description or codebase, identify:
- Components and GCP services involved
- Connections, protocols, and data flow direction
- Logical groupings (which services belong together)
- Diagram type (system overview, agent hierarchy, data flow, schema, deployment, security)

### 2. Build the Prompt

Read [references/gcp-brand.md](references/gcp-brand.md) for colors, typography, and icon guidelines. Select and fill a template from [references/templates.md](references/templates.md).

Every prompt must include these phrases:
- "professional, clean architecture diagram in the style of official Google Cloud Platform documentation"
- "GCP brand colors: blue (#4285F4), green (#34A853), yellow (#FBBC05), red (#EA4335)"
- "clean white background"
- "Google Cloud product icon style, clean lines, no 3D effects, no hexagons, modern flat design"
- "Google Cloud logo watermark at bottom left"

Color conventions by component type:
- **Compute/Agents**: Green (#34A853)
- **Data/Analytics/BigQuery**: Orange/Yellow (#F9AB00)
- **AI/ML/Vertex AI**: Purple (#A142F4)
- **Storage/GCS**: Yellow (#FBBC05)
- **Networking/Serverless**: Teal (#12B5CB)
- **Security**: Red (#EA4335)
- **Discovery Engine/Search**: Blue (#4285F4)
- **Users/Clients**: Red ellipse (#EA4335)
- **Config/Infrastructure**: Gray (#5F6368)

### 3. Generate

Try the PaperBanana MCP tool first (`mcp__paperbanana__generate_diagram`). If unavailable, use Vertex AI directly:

```python
from google import genai
from google.genai import types

client = genai.Client(vertexai=True, project=PROJECT_ID, location="us-central1")
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",  # fallback: "gemini-2.5-flash-image"
    contents=prompt,
    config=types.GenerateContentConfig(response_modalities=["IMAGE", "TEXT"]),
)
for part in response.candidates[0].content.parts:
    if part.inline_data:
        with open(output_path, "wb") as f:
            f.write(part.inline_data.data)
```

Model priority: `gemini-3-pro-image-preview` > `gemini-2.5-flash-image`. Fall back on 404.

### 4. Review

Verify before delivering:
- All components labeled correctly
- Connections directional with protocols noted
- Colors consistent with GCP brand conventions
- **Spelling**: Double-check every label, service name, and annotation for typos. Compare against official GCP product names (e.g., "BigQuery" not "Big Query", "Cloud Run" not "CloudRun", "Vertex AI" not "VertexAI"). Read every word in the prompt one more time before generating.
- Text readable at expected display size
- Layout balanced, no overlapping elements
- All shapes are rounded rectangles, circles, or ellipses — never hexagons

Regenerate with refined prompt if any issues found.

## Prompt Tips

- Specify layout: "top-to-bottom" or "left-to-right"
- Use shape hints: "rounded rectangle" (services), "cylinder" (databases), "ellipse" (users), "octagon" (security), "folder" (storage)
- Name every connection with its protocol
- Add "landscape orientation" for wide architectures
- Include resource IDs and regions for deployed resources

## References

- **GCP brand colors, typography, icons**: [references/gcp-brand.md](references/gcp-brand.md)
- **Prompt templates by diagram type**: [references/templates.md](references/templates.md)
- **GCP Product Icons PDF**: https://services.google.com/fh/files/misc/google-cloud-product-icons.pdf
- **GCP Icons Gallery**: https://cloud.google.com/icons
