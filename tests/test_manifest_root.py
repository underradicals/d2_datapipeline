from models import ManifestRoot
from pathlib import Path


ROOT = Path(__file__).parent.parent
MANIFEST_PATH = ROOT / "manifest.json"


def test_version_exists():
    with open(MANIFEST_PATH) as manifest_file:
        manifest = manifest_file.read()
        manifest_model = ManifestRoot.model_validate_json(manifest)
        assert manifest_model.Response.version == "236360.25.08.20.2000-2-bnet.61533"
