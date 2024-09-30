import Modal from "react-bootstrap/Modal";
import React from "react";
import Button from "react-bootstrap/Button";

function ModalEditDriveDisc(props) {
  const { show, handleClose } = props;
  return (
    <div>
      <Modal
        className="wEngine-modal-container"
        show={show}
        onHide={handleClose}
        backdrop={"static"}
        keyboard={false}
        size="xl"
      >
        <Modal.Header className="modal-header">
          <h4>Drive Disc Editor</h4>
          <Button variant="secondary" onClick={handleClose}>
            X
          </Button>
        </Modal.Header>

        <Modal.Body className="drivedisc-modal-body">
          {/* Left Display */}
          <div className="col-lg-6">
            {/* Set and Rarity selection */}
            <div class="artifact-header">
              <div className="input-holder">
                <input
                  id="field-set"
                  name="field-set"
                  type="text"
                  placeholder="Unknown set"
                  className="col-lg-11"
                />

                <button className="col-lg-1">
                  <i class="bi bi-arrow-down"></i>
                </button>
              </div>

              <button className=" select-rarity">
                Rarity{" "}
                <span>
                  <i class="bi bi-arrow-down"></i>
                </span>
              </button>
            </div>
            {/* Select level */}
            <div class="artifact-level">
              <div class="drivedisk-level-container col-lg-5">
                <label for="drivedisk-level-input">Level</label>
                <input
                  type="number"
                  id="drivedisk-level-input"
                  class="drivedisk-level-input"
                  min="1"
                  max="15"
                  placeholder="0"
                />
              </div>
              <div class="quick-level-select col-lg-7">
                <button>-</button>
                <button>0</button>
                <button>3</button>
                <button>6</button>
                <button>9</button>
                <button>12</button>
                <button>15</button>
                <button>+</button>
              </div>
            </div>
            {/* Select slot */}
            <button className="select-slot">Select partition</button>

            {/* Select Main Stat */}
            <div className="main-stat-display">
              <button className=" main-stat-select">
                HP
                <span>
                  <i class="bi bi-arrow-down"></i>
                </span>
              </button>

              <div className="main-stat">2000</div>
            </div>
          </div>

          {/* Right Display */}
          <div className="col-lg-6">
            {
              <>
                {" "}
                {/* First sub stat */}
                <div className="sub-stat">
                  <div className="sub-stat-header">
                    <button className="sub-stat-selection">Substat 1</button>
                    <div className="sub-stat-display">0</div>
                  </div>
                  <div className="sub-stat-body">
                    <input
                      type="range"
                      id="subStat1"
                      name="subStat1"
                      min="0"
                      max="11"
                      step={1}
                    />
                  </div>
                </div>
                {/*  Second */}
                <div className="sub-stat">
                  <div className="sub-stat-header">
                    <button className="sub-stat-selection">Substat 2</button>
                    <div className="sub-stat-display">0</div>
                  </div>
                  <div className="sub-stat-body">
                    <input
                      type="range"
                      id="subStat2"
                      name="subStat2"
                      min="0"
                      max="11"
                      step={1}
                    />
                  </div>
                </div>
                {/* Third */}
                <div className="sub-stat">
                  <div className="sub-stat-header">
                    <button className="sub-stat-selection">Substat 3</button>
                    <div className="sub-stat-display">0</div>
                  </div>
                  <div className="sub-stat-body">
                    <input
                      type="range"
                      id="subStat3"
                      name="subStat3"
                      min="0"
                      max="11"
                      step={1}
                    />
                  </div>
                </div>
                {/* Fourth */}
                <div className="sub-stat">
                  <div className="sub-stat-header">
                    <button className="sub-stat-selection">Substat 4</button>
                    <div className="sub-stat-display">0</div>
                  </div>
                  <div className="sub-stat-body">
                    <input
                      type="range"
                      id="subStat4"
                      name="subStat4"
                      min="0"
                      max="11"
                      step={1}
                    />
                  </div>
                </div>
              </>
            }
          </div>
        </Modal.Body>

        <Modal.Footer className="modal-footer no-border">
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default ModalEditDriveDisc;
