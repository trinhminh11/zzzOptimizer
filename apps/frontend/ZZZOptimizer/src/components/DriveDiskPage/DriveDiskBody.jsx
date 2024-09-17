import React, { useState } from "react";
import "./driveDisk.css";
import ModalEditDriveDisc from "./ModalEditDriveDisc";

function DriveDiskBody() {
  const [isShowModalEdit, setShowModalEdit] = useState(false);
  const [dataDriveDiscEdit, setDataDriveDiscEdit] = useState([]);

  const handleClose = () => {
    setShowModalEdit(false);
  };

  const handleAddNewDriveDisc = () => {
    setShowModalEdit(true);
  };

  return (
    <div className="drive-disc-container">
      <button className="add-disk-btn" onClick={handleAddNewDriveDisc}>
        Add a Drive Disk
      </button>

      <ModalEditDriveDisc show={isShowModalEdit} handleClose={handleClose} />
    </div>
  );
}

export default DriveDiskBody;
