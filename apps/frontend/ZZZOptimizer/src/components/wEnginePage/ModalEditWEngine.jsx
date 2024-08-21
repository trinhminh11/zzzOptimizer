import { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import parse from "html-react-parser";
import "./wEngine.css";

export default function ModalEditEngine(props) {
  const { show, handleClose, dataWEngineEdit, removeWEngine } = props;
  let passiveDescription = dataWEngineEdit.passive;
  return (
    <div>
      <Modal
        className="wEngine-modal-container"
        show={show}
        onHide={handleClose}
        backdrop={"static"}
        keyboard={false}
        size="lg"
        centered
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

        <Modal.Body className="wEngine-modal-body">
          <div className="col-lg-4">
            <div className={"wEngine-left-img agent-" + dataWEngineEdit.rank}>
              <img src={dataWEngineEdit.nameIcon} alt="" />
            </div>
          </div>
          <div className="col-lg-8">
            <div>{parse(String(passiveDescription))}</div>
            <div>
              <table class="table table-bordered table-dark stat-table">
                <thead>
                  <tr>
                    <td scope="col" colspan="2">
                      Main Stat
                    </td>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Mark</td>
                    <td>Otto</td>
                  </tr>
                  <tr>
                    <td>Jacob</td>
                    <td>Thornton</td>
                  </tr>
                </tbody>
              </table>
            </div>
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
