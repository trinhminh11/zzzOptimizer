import { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import { getWEngineStats as fetchWEngineStats } from "../../services/WEngineService";
import { getWEngineDescription as fetchWEngineDescription } from "../../services/WEngineService";

import parse from "html-react-parser";
import "./wEngine.css";

export default function ModalEditEngine(props) {
  const {
    show,
    handleClose,
    dataWEngineEdit,
    removeWEngine,
    subStatMap,
    selectedLevel,
    setSelectedLevel,
    selectedUpgrade,
    setSelectedUpgrade,
    selectedModification,
    setSelectedModification,
  } = props;
  const [wEngineStat, setWEngineStat] = useState([]);
  const [wEngineDescription, setWEngineDescription] = useState([]);

  const getWEngineStats = async () => {
    let stat = await fetchWEngineStats(
      dataWEngineEdit.name,
      selectedModification,
      selectedLevel
    );
    if (stat) {
      setWEngineStat(stat);
      dataWEngineEdit.mainStat[1] = stat.mainStat[1];
      dataWEngineEdit.subStat[1] = stat.subStat[1];
    }
  };

  const getWEngineDescription = async () => {
    let description = await fetchWEngineDescription(
      dataWEngineEdit.name,
      selectedUpgrade
    );
    if (description) {
      setWEngineDescription(description.passive);
      dataWEngineEdit.passive = description.passive;
    }
  };
  // W-Engine Description
  //let passiveDescription = dataWEngineEdit.passive;
  let passiveDescription = dataWEngineEdit.passive;

  // Set up open state for upgrade dropdown
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  // Set up open state for level dropdown
  const [isLevelDropdownOpen, setIsLevelDropdownOpen] = useState(false);

  // Set up open state for modification dropdown
  const [isModificationDropdownOpen, setIsModificationDropdownOpen] =
    useState(false);

  // Handle the open function for upgrade select button
  const handleUpgradeButtonClick = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  // Set up the open function for level select button
  const handleLevelButtonClick = () => {
    setIsLevelDropdownOpen(!isLevelDropdownOpen);
  };

  const handleModificationButtonClick = () => {
    if (selectedLevel % 10 === 0) {
      setIsModificationDropdownOpen(!isModificationDropdownOpen);
    }
  };

  // Handle when a upgrade is chose
  const handleOptionClick = (option) => {
    setSelectedUpgrade(option);
    setIsDropdownOpen(false);
  };

  // Handle when a level is chose
  const handleLevelOptionClick = (option) => {
    setSelectedLevel(option);
    setIsLevelDropdownOpen(false);

    // Automatically set modification if the level is not a multiple of 10

    if (option % 10 !== 0) {
      setSelectedModification(Math.floor(option / 10));
      setIsModificationDropdownOpen(false); // Close modification dropdown if it's not needed
    } else {
      // If the level is a multiple of 10, allow the user to choose between two options
      if (option == 60) {
        setSelectedModification(5);
      } else {
        setSelectedModification(Math.floor(option / 10));
        setIsModificationDropdownOpen(true); // Open modification dropdown for selection
      }
    }
  };

  // Handle when a modification is chose
  const handleModificationOptionClick = (option) => {
    setSelectedModification(option);
    setIsModificationDropdownOpen(false);
  };

  // Handle when press enter on level input
  const handleLevelInputKeyDown = (e) => {
    if (e.key == "Enter") {
      const level = parseInt(e.target.value, 10);
      changeModification(level);
    }
  };

  // Handle when the level is changed
  const handleLevelChanged = (level) => {
    setSelectedLevel(level);
    changeModification(level);
  };

  const changeModification = (level) => {
    // Update the modification based on the level
    if (level < 10) {
      setSelectedModification(0);
    } else if (level == 60) {
      setSelectedModification(5);
    } else if (level % 10 !== 0) {
      setSelectedModification(Math.floor(level / 10));
    } else {
      setSelectedModification(Math.floor(level / 10)); // Default choice when level is a multiple of 10
      setIsModificationDropdownOpen(true); // Optionally open the modification dropdown for selection
    }
  };

  const handleConfirmButtonClick = async () => {
    await getWEngineStats();
    await getWEngineDescription();
    dataWEngineEdit.level = selectedLevel;
    dataWEngineEdit.upgrade = selectedUpgrade;
    dataWEngineEdit.modification = selectedModification;
    // Get the current list from localStorage
    const savedData = localStorage.getItem("selected wEngine");
    const currentList = savedData ? JSON.parse(savedData) : [];

    // Find the index of the WEngine being edited
    const index = currentList.findIndex(
      (wEngine) => wEngine.name === dataWEngineEdit.name
    );

    // Update the WEngine in the list
    if (index !== -1) {
      currentList[index] = dataWEngineEdit;
    } else {
      currentList.push(dataWEngineEdit);
    }

    // Save the updated list back to localStorage
    localStorage.setItem("selected wEngine", JSON.stringify(currentList));

    console.log("Updated dataWEngineEdit:", dataWEngineEdit);
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
              {/* Upgrade */}
              <div className="dropdown">
                <button
                  className="dropdown-button"
                  onClick={handleUpgradeButtonClick}
                >
                  Upgrade {selectedUpgrade}
                </button>
                {isDropdownOpen && (
                  <div className="dropdown-content">
                    <div onClick={() => handleOptionClick("0")}>Upgrade 0</div>
                    <div onClick={() => handleOptionClick("1")}>Upgrade 1</div>
                    <div onClick={() => handleOptionClick("2")}>Upgrade 2</div>
                    <div onClick={() => handleOptionClick("3")}>Upgrade 3</div>
                    <div onClick={() => handleOptionClick("4")}>Upgrade 4</div>
                    <div onClick={() => handleOptionClick("5")}>Upgrade 5</div>
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
                    value={selectedLevel}
                    onChange={(e) => handleLevelChanged(e.target.value)}
                    onKeyDown={handleLevelInputKeyDown}
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

                {/* Choose Modification */}
                <div className="level-dropdown">
                  <button
                    className="level-dropdown-button"
                    onClick={handleModificationButtonClick}
                  >
                    Modification {selectedModification}
                  </button>
                  {isModificationDropdownOpen && (
                    <div className="level-dropdown-content">
                      <div
                        onClick={() =>
                          handleModificationOptionClick(
                            Math.floor(selectedLevel / 10)
                          )
                        }
                      >
                        Upgrade {Math.floor(selectedLevel / 10)}
                      </div>
                      <div
                        onClick={() =>
                          handleModificationOptionClick(
                            Math.floor(selectedLevel / 10) - 1
                          )
                        }
                      >
                        Upgrade {Math.floor(selectedLevel / 10) - 1}
                      </div>
                    </div>
                  )}
                </div>
              </div>

              {/* Confirm Button */}
              <button
                className="confirm-lv-button"
                onClick={handleConfirmButtonClick}
              >
                Confirm
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
                    <td>
                      {dataWEngineEdit.mainStat
                        ? subStatMap.get(dataWEngineEdit.mainStat[0])
                        : 0}
                    </td>
                    <td>
                      {dataWEngineEdit.mainStat
                        ? dataWEngineEdit.mainStat[1]
                        : 0}
                    </td>
                  </tr>
                  <tr>
                    <td>
                      {dataWEngineEdit.subStat
                        ? subStatMap.get(dataWEngineEdit.subStat[0])
                        : 0}
                    </td>
                    <td>
                      {dataWEngineEdit.subStat ? dataWEngineEdit.subStat[1] : 0}
                    </td>
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
