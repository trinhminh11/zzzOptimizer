import { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

import parse from "html-react-parser";
import "./wEngine.css";

export default function ModalEditEngine(props) {
  const { show, handleClose, dataWEngineEdit, removeWEngine } = props;
  let passiveDescription = dataWEngineEdit.passive;

  const [selectedRefinement, setSelectedRefinement] =
    useState("Select Refinement");

  const [selectedLevel, setSelectedLevel] = useState(0);

  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const [isLevelDropdownOpen, setIsLevelDropdownOpen] = useState(false);

  const handleRefinementButtonClick = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  const handleLevelButtonClick = () => {
    setIsLevelDropdownOpen(!isLevelDropdownOpen);
  };

  const handleOptionClick = (option) => {
    setSelectedRefinement(option);
    setIsDropdownOpen(false);
  };

  const handleLevelOptionClick = (option) => {
    setSelectedLevel(option);
    setIsLevelDropdownOpen(false);
  };
  return (
    <div>
      <Modal
        className="wEngine-modal-container"
        show={show}
        onHide={handleClose}
        backdrop={"static"}
        keyboard={false}
        size="lg"
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
          {/* Left Diplay */}
          <div className="col-lg-4">
            <div className={"wEngine-left-img agent-" + dataWEngineEdit.rank}>
              <img src={dataWEngineEdit.nameIcon} alt="" />
            </div>

            <div className="level-display">
              {/* Refinement */}
              <div className="dropdown">
                <button
                  className="dropdown-button"
                  onClick={handleRefinementButtonClick}
                >
                  {selectedRefinement}
                </button>
                {isDropdownOpen && (
                  <div className="dropdown-content">
                    <div onClick={() => handleOptionClick("Refinement 0")}>
                      Refinement 0
                    </div>
                    <div onClick={() => handleOptionClick("Refinement 1")}>
                      Refinement 1
                    </div>
                    <div onClick={() => handleOptionClick("Refinement 2")}>
                      Refinement 2
                    </div>
                    <div onClick={() => handleOptionClick("Refinement 3")}>
                      Refinement 3
                    </div>
                    <div onClick={() => handleOptionClick("Refinement 4")}>
                      Refinement 4
                    </div>
                    <div onClick={() => handleOptionClick("Refinement 5")}>
                      Refinement 5
                    </div>
                  </div>
                )}
              </div>

              {/* Level */}

              <div class="level-container">
                <div class="level-input">
                  <label for="level">Level</label>
                  <input
                    type="number"
                    id="level"
                    name="level"
                    min="1"
                    max="60"
                    placeholder={selectedLevel}
                  ></input>
                </div>

                <div class="level-dropdown">
                  <button
                    class="level-dropdown-button"
                    onClick={handleLevelButtonClick}
                  >
                    Select Level ▾
                  </button>
                  {isLevelDropdownOpen && (
                    <div class="level-dropdown-content">
                      <div onClick={() => handleLevelOptionClick(10)}>10</div>
                      <div onClick={() => handleLevelOptionClick(20)}>20</div>
                      <div onClick={() => handleLevelOptionClick(30)}>30</div>
                      <div onClick={() => handleLevelOptionClick(40)}>40</div>
                      <div onClick={() => handleLevelOptionClick(50)}>50</div>
                      <div onClick={() => handleLevelOptionClick(60)}>60</div>
                    </div>
                  )}
                </div>
              </div>

              {/* Confirm Button */}
              <button className="confirm-lv-button">Comfirm</button>
            </div>
          </div>

          {/* Right Display */}
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
