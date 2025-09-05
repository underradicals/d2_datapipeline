from pydantic import BaseModel


class ManifestResponse(BaseModel):
    version: str


class ManifestRoot(BaseModel):
    Response: ManifestResponse
