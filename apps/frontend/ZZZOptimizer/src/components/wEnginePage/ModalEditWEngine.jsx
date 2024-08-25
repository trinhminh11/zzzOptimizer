import { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import { getWEngineStats as fetchWEngineStats } from "../../services/WEngineService";

import parse from "html-react-parser";
import "./wEngine.css";

export default function ModalEditEngine(props) {
  const {
    show,
    handleClose,
    dataWEngineEdit,
    removeWEngine,
    subStatMap,
    wEngineStat,
    setWEngineStat,
  } = props;
  // const [wEngineStat, setWEngineStat] = useState([]);

  const getWEngineStats = async () => {
    let stat = await fetchWEngineStats(
      dataWEngineEdit.name,
      Math.floor(selectedLevel / 10),
      selectedLevel
    );
    if (stat) {
      setWEngineStat(stat);
    }
  };

  // W-Engine Description
  let passiveDescription = dataWEngineEdit.passive;

  // Set up var to store selected refinement
  const [selectedRefinement, setSelectedRefinement] =
    useState("Select Refinement");

  // Set up var to store selected level
  const [selectedLevel, setSelectedLevel] = useState(0);

  // Set up open state for refinement dropdown
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  // Set up open state for level dropdown
  const [isLevelDropdownOpen, setIsLevelDropdownOpen] = useState(false);

  // Handle the open function for refinement select button
  const handleRefinementButtonClick = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  // Set up the open function for level select button
  const handleLevelButtonClick = () => {
    setIsLevelDropdownOpen(!isLevelDropdownOpen);
  };

  // Handle when a refinement is chose
  const handleOptionClick = (option) => {
    setSelectedRefinement(option);
    setIsDropdownOpen(false);
  };

  // Handle when a level is chose
  const handleLevelOptionClick = (option) => {
    setSelectedLevel(option);
    setIsLevelDropdownOpen(false);
  };

  const handleConfirmButtonClick = () => {
    getWEngineStats();
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

              <div className="level-container">
                <div className="level-input">
                  <label htmlFor="level">Level</label>
                  <input
                    type="number"
                    id="level"
                    name="level"
                    min="1"
                    max="60"
                    placeholder={selectedLevel}
                    value={selectedLevel}
                    onChange={(e) => setSelectedLevel(e.target.value)}
                  ></input>
                </div>

                <div className="level-dropdown">
                  <button
                    className="level-dropdown-button"
                    onClick={handleLevelButtonClick}
                  >
                    Select Level ▾
                  </button>
                  {isLevelDropdownOpen && (
                    <div className="level-dropdown-content">
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
              <button
                className="confirm-lv-button"
                onClick={handleConfirmButtonClick}
              >
                Comfirm
              </button>
            </div>
          </div>

          {/* Right Display */}
          <div className="col-lg-8">
            <div>{parse(String(passiveDescription))}</div>
            <div>
              <table className="table table-bordered table-dark stat-table">
                <thead>
                  <tr>
                    <td scope="col" colSpan="2">
                      WEngine Stats
                    </td>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>{subStatMap.get(wEngineStat.mainStat[0])}</td>
                    <td>{wEngineStat.mainStat[1]}</td>
                  </tr>
                  <tr>
                    <td>{subStatMap.get(wEngineStat.subStat[0])}</td>
                    <td>{wEngineStat.subStat[1]}</td>
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
        </Modal.Footer>
      </Modal>
    </div>
  );
}
