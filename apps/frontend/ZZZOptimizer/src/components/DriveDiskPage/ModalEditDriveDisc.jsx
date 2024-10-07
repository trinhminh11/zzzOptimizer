import Modal from "react-bootstrap/Modal";
import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import util from "../../util";

function ModalEditDriveDisc(props) {
  const { show, handleClose, listDriveDiscs, listDriveDiscsProperty } = props;

  // Start setting up for set selection
  const [driveDiskNameSearch, setDriveDiskNameSearch] = useState(""); // User's search term
  const [selectedDiscName, setSelectedDiscName] = useState("Unknown set"); // Selected disc
  const [showNameSelectDropdown, setShowNameSelectDropdown] = useState(false); // Control dropdown visibility

  // Control dropdown visibility for rarity selection
  const [showRaritySelectionDropdown, setShowRaritySelectionDropdown] =
    useState(false);

  // Partition selection
  const [selectedPartition, setSelectedPartition] =
    useState("Select partition"); // Selected partition
  const [showPartitionDropdown, setShowPartitionDropdown] = useState(false); // Control partition dropdown visibility

  // Rarity selection
  const [selectedRarity, setSelectedRarity] = useState("Select Rarity"); // Selected rarity
  const [selectedLevel, setSelectedLevel] = useState(""); // State for selected level

  // Main Stat selection
  const [showMainStatDropdown, setShowMainStatDropdown] = useState(false);
  const [selectedMainStat, setSelectedMainStat] = useState("Select Main Stat");
  const [availableMainStats, setAvailableMainStats] = useState([]);
  const [mainStatValue, setMainStatValue] = useState(0);

  // Filter the discs based on the search term
  const filteredDiscs = driveDiskNameSearch
    ? listDriveDiscs.filter((disc) =>
        disc.name.toLowerCase().includes(driveDiskNameSearch.toLowerCase())
      )
    : listDriveDiscs; // Show all discs if no search term is provided

  // Handle disc name selection
  const handleSelectDisc = (disc) => {
    setSelectedDiscName(disc.name); // Set selected name as input value
    setDriveDiskNameSearch(""); // Clear the search input after selection
    setShowNameSelectDropdown(false); // Close the dropdown after selection
  };

  // Handle rarity selection
  const handleSelectRarity = (rarity) => {
    setSelectedRarity(rarity); // Set the selected rarity
    setShowRaritySelectionDropdown(false); // Close the dropdown after selection
  };

  // Handle level selection and update input
  const handleSelectLevel = (level) => {
    setSelectedLevel(level); // Set the selected level
  };

  // Determine the maximum level based on selected rarity
  const getMaxLevel = () => {
    switch (selectedRarity) {
      case "S":
        return 15;
      case "A":
        return 12;
      case "B":
        return 9;
      default:
        return 15; // Default max level
    }
  };

  // Handle manual level input
  const handleLevelInputChange = (e) => {
    const value = parseInt(e.target.value, 10); // Parse the input value to an integer
    if (!isNaN(value) && value >= 0 && value <= getMaxLevel()) {
      setSelectedLevel(value); // Update state with the parsed value if it's a valid number
    } else {
      setSelectedLevel(""); // Clear the input if the value is invalid
    }
  };

  // Handle partition selection
  const handleSelectPartition = (partition) => {
    setSelectedPartition(partition);
    setShowPartitionDropdown(false);

    // Set available main stats based on selected partition
    const partitionNumber = parseInt(partition.split(" ")[1]); // Extract the number from "Partition X"
    if (partitionNumber >= 1 && partitionNumber <= 6) {
      setAvailableMainStats(
        listDriveDiscsProperty.availabelMainStats[partitionNumber]
      );
    }
  };

  // Handle main stat selection
  const handleMainStatSelect = async (stat, selectedRarity, selectedLevel) => {
    await setSelectedMainStat(stat); // Set selected main stat
    await setShowMainStatDropdown(false);
    handleUpdateMainStat(selectedMainStat, selectedRarity, selectedLevel);
  };

  const handleUpdateMainStat = (
    selectedMainStat,
    selectedRarity,
    selectedLevel
  ) => {
    const value =
      listDriveDiscsProperty.mainStatBase[selectedRarity][selectedMainStat];

    const increment =
      listDriveDiscsProperty.mainStatIncrement[selectedRarity][
        selectedMainStat
      ];

    const valueWithIncrement = value + increment * selectedLevel;

    setMainStatValue(valueWithIncrement);
    console.log(increment);
  };

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
            <div className="artifact-header">
              <div className="input-holder" style={{ position: "relative" }}>
                <input
                  id="field-set"
                  name="field-set"
                  type="text"
                  placeholder="Select a disc" // General placeholder
                  className="col-lg-11"
                  value={driveDiskNameSearch || selectedDiscName} // Use selected name if search is empty
                  onClick={() => setShowNameSelectDropdown(true)} // Always open dropdown on click
                  onChange={(e) => setDriveDiskNameSearch(e.target.value)} // Update search term
                />

                <button
                  className="col-lg-1 arrow-down"
                  onClick={() =>
                    setShowNameSelectDropdown(!showNameSelectDropdown)
                  }
                >
                  <i className="bi bi-arrow-down"></i>
                </button>

                {/* DropDown */}
                {showNameSelectDropdown && (
                  <div className="name-dropdown-menu ">
                    {filteredDiscs.length > 0 ? (
                      filteredDiscs.map((disc, index) => (
                        <button
                          key={index}
                          className="name-select-dropdown-item"
                          onClick={() => handleSelectDisc(disc)}
                        >
                          {disc.name}
                        </button>
                      ))
                    ) : (
                      <div className="name-select-dropdown-item no-matches">
                        No matches
                      </div>
                    )}
                  </div>
                )}
              </div>

              <div className="rarity-container">
                <button
                  className=" select-rarity"
                  onClick={() => setShowRaritySelectionDropdown(true)}
                >
                  {selectedRarity ? (
                    <img
                      src={util.wEngineRankIcon[selectedRarity]}
                      alt={`Rank ${selectedRarity}`}
                      style={{ width: "30px", height: "30px" }}
                    />
                  ) : (
                    "Select Rarity"
                  )}
                  {!selectedRarity && (
                    <span>
                      <i className="bi bi-arrow-down"></i>
                    </span>
                  )}
                </button>

                {showRaritySelectionDropdown && (
                  <div className="rarity-dropdown-menu">
                    {["S", "A", "B"].map((rarity, index) => (
                      <button
                        key={index}
                        className="rarity-select-dropdown-item"
                        onClick={() => handleSelectRarity(rarity)}
                      >
                        Rank {rarity}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>

            {/* Select level */}
            <div className="artifact-level">
              <div className="drivedisk-level-container col-lg-6">
                <label htmlFor="drivedisk-level-input">Level</label>
                <input
                  type="number"
                  id="drivedisk-level-input"
                  className="drivedisk-level-input"
                  min="0" // Start from 0
                  max={getMaxLevel()} // Set max level based on rarity
                  value={selectedLevel} // The selected level is reflected here
                  placeholder="0"
                  onChange={handleLevelInputChange} // Use the new input handler
                />
              </div>
              <div className="quick-level-select col-lg-6">
                {[0, 3, 6, 9, 12, 15].map((level) => (
                  <button
                    key={level}
                    onClick={() => handleSelectLevel(level)}
                    disabled={level > getMaxLevel()} // Disable button if level is above max allowed
                    style={{
                      backgroundColor: level > getMaxLevel() ? "gray" : "", // Set background color to gray if disabled
                      color: level > getMaxLevel() ? "white" : "", // Change text color for better visibility
                      cursor: level > getMaxLevel() ? "not-allowed" : "pointer", // Change cursor style
                    }}
                  >
                    {level}
                  </button>
                ))}
              </div>
            </div>

            {/* Select partition */}
            <div className="partition-selection">
              <button
                className="select-slot"
                onClick={() => setShowPartitionDropdown(!showPartitionDropdown)}
              >
                {selectedPartition}
                <span>
                  <i className="bi bi-arrow-down"></i>
                </span>
              </button>

              {showPartitionDropdown && (
                <div className="partition-dropdown-menu">
                  {[1, 2, 3, 4, 5, 6].map((partition) => (
                    <button
                      key={partition}
                      className="partition-select-dropdown-item"
                      onClick={() =>
                        handleSelectPartition(`Partition ${partition}`)
                      }
                    >
                      Partition {partition}
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* Select Main Stat */}
            <div className="main-stat-display">
              {availableMainStats.length === 1 ? (
                // If only one main stat available, display it directly
                <button
                  className="main-stat-select"
                  onClick={() =>
                    handleMainStatSelect(
                      availableMainStats[0],
                      selectedRarity,
                      selectedLevel
                    )
                  }
                >
                  {availableMainStats[0]}
                </button>
              ) : (
                // If multiple stats are available, show dropdown
                <button
                  className="main-stat-select"
                  onClick={() => setShowMainStatDropdown(!showMainStatDropdown)}
                >
                  {selectedMainStat}
                  <span>
                    <i className="bi bi-arrow-down"></i>
                  </span>
                </button>
              )}

              {/* Dropdown for main stats if there are multiple options */}
              {availableMainStats.length > 1 && showMainStatDropdown && (
                <div className="main-stat-dropdown-menu">
                  {availableMainStats.map((stat, index) => (
                    <button
                      key={index}
                      className="main-stat-dropdown-item"
                      onClick={() =>
                        handleMainStatSelect(
                          stat,
                          selectedRarity,
                          selectedLevel
                        )
                      }
                    >
                      {stat}
                    </button>
                  ))}
                </div>
              )}

              <div className="main-stat">{mainStatValue}</div>
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
          <button variant="secondary" className="add-btn">
            Add Drive Disc
          </button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default ModalEditDriveDisc;
