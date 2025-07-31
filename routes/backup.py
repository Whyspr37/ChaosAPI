from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from utils.drive_backup import zip_and_upload_to_drive, mirror_and_upload_to_drive

router = APIRouter()

@router.post("/backup_to_drive")
async def backup_to_drive(mode: str = "zip"):
    """
    Trigger a manual backup to Google Drive.
    mode: "zip" for zipped archive or "mirror" for direct folder structure copy.
    """
    try:
        if mode == "zip":
            drive_link = zip_and_upload_to_drive()
        elif mode == "mirror":
            drive_link = mirror_and_upload_to_drive()
        else:
            raise HTTPException(status_code=400, detail="Invalid mode. Use 'zip' or 'mirror'.")

        return JSONResponse({
            "message": "Backup uploaded successfully",
            "drive_link": drive_link
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Drive backup failed: {str(e)}")