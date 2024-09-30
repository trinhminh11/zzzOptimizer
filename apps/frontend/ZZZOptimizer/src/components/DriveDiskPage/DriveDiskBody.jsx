import React, { useState, useEffect } from "react";
import "./driveDisk.css";
import ModalEditDriveDisc from "./ModalEditDriveDisc";
import { DriveDiscService } from "../../services/DriveDiscService";

function DriveDiskBody() {
  const [isShowModalEdit, setShowModalEdit] = useState(false);
  const [dataDriveDiscEdit, setDataDriveDiscEdit] = useState([]);

  // set up list for storing Drive Disc from api
  const [listDriveDiscs, setListDriveDiscs] = useState([]);

  // set up local storage for storing information
  const [listSelectedDriveDiscs, setListSelectedDriveDiscs] = useState(() => {
    //Check local storage and initialize list
    const storedDriveDiscs = localStorage.getItem("drivediscs");
    return storedDriveDiscs ? JSON.parse(storedDriveDiscs) : [];
  });

  // Set up function for storing data from api into the list
  useEffect(() => {
    getDriveDiscs();
  }, []);

  const getDriveDiscs = async () => {
    let res = await DriveDiscService();
    if (res) {
      setListDriveDiscs(res);
    }
  };

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

      <ModalEditDriveDisc
        show={isShowModalEdit}
        handleClose={handleClose}
        listDriveDiscs={listDriveDiscs}
      />
    </div>
  );
}

export default DriveDiskBody;
