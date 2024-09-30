import Modal from "react-bootstrap/Modal";
import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";

function ModalEditDriveDisc(props) {
  const { show, handleClose, listDriveDiscs } = props;

  // Start setting up for set selection
  const [driveDiskNameSearch, setDriveDiskNameSearch] = useState(""); // User's search term
  const [selectedDiscName, setSelectedDiscName] = useState("Unknown set"); // Selected disc
  const [showNameSelectDropdown, setShowNameSelectDropdown] = useState(false); // Control dropdown visibility

  // Filter the discs based on the search term
  const filteredDiscs = driveDiskNameSearch
    ? listDriveDiscs.filter((disc) =>
        disc.name.toLowerCase().includes(driveDiskNameSearch.toLowerCase())
      )
    : listDriveDiscs; // Show all discs if no search term is provided

  // Handle disc selection
  const handleSelectDisc = (disc) => {
    setSelectedDiscName(disc.name); // Set selected name as input value
    setDriveDiskNameSearch(""); // Clear the search input after selection
    setShowNameSelectDropdown(false); // Close the dropdown after selection
  };

  // End setting up for set selection

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

              <button className=" select-rarity">
                Rarity{" "}
                <span>
                  <i className="bi bi-arrow-down"></i>
                </span>
              </button>
            </div>
            {/* Select level */}
            <div className="artifact-level">
              <div className="drivedisk-level-container col-lg-5">
                <label for="drivedisk-level-input">Level</label>
                <input
                  type="number"
                  id="drivedisk-level-input"
                  className="drivedisk-level-input"
                  min="1"
                  max="15"
                  placeholder="0"
                />
              </div>
              <div className="quick-level-select col-lg-7">
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
          <button variant="secondary" className="add-btn">
            Add Drive Disc
          </button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default ModalEditDriveDisc;
