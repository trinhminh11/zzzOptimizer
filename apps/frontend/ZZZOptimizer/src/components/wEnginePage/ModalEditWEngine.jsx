import { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import "./wEngine.css";

export default function ModalEditEngine(props) {
  const { show, handleClose, dataWEngineEdit, removeWEngine } = props;
  return (
    <div>
      <Modal
        className="modal-container"
        show={show}
        onHide={handleClose}
        backdrop={"static"}
        keyboard={false}
      >
        <Modal.Header className="modal-header">
          <h4>{dataWEngineEdit.name}</h4>
          <button
            className="btn btn-danger"
            onClick={() => removeWEngine(dataWEngineEdit.name)}
          >
            Remove WEngine
          </button>
        </Modal.Header>

        <Modal.Body className="modal-body"></Modal.Body>
        <Modal.Footer className="modal-footer no-border">
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          {/* <Button variant="primary" onClick={() => handleEditUser()}>
            Confirm
          </Button> */}
        </Modal.Footer>
      </Modal>
    </div>
  );
}
