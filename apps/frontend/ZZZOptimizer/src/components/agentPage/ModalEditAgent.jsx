import { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import "./agent.css";

export default function ModalEditAgent(props) {
  const { show, handleClose, dataAgentEdit } = props;
  return (
    <div>
      <Modal
        show={show}
        onHide={handleClose}
        backdrop={"static"}
        keyboard={false}
        className="modal-container"
      >
        <Modal.Header closeButton className="modal-header no-border">
          <h4>{dataAgentEdit.realName}</h4>
        </Modal.Header>
        <Modal.Body className="modal-body no-border">
          <div className="modal-left">{/* Character Image and Stats */}</div>
          <div className="modal-right">
            {/* Artifact Slots */}
            <div className="item-card">Artifact 1</div>
            <div className="item-card">Artifact 2</div>
            <div className="item-card">Artifact 3</div>
            <div className="item-card">Artifact 4</div>
            <div className="item-card">Artifact 5</div>
            <div className="item-card">Artifact 6</div>
          </div>
        </Modal.Body>
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
