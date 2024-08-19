import React from "react";
import "./wEngine.css";
import { useEffect, useState } from "react";
import ModalEditWEngine from "./ModalEditWEngine";

function WEngineLocalDatabase({
  listSelectedWEngines,
  setListSelectedWEngines,
  selectedOptions,
}) {
  // Init variable for wEngine edit show function
  const [isShowModalEdit, setShowModalEdit] = useState(false);
  const [dataWEngineEdit, setDataWEnigineEdit] = useState([]);

  // Closing function for ModalEditAgent
  const handleClose = () => {
    setShowModalEdit(false);
  };

  // Edit agent function
  const handleEditWEngine = (wEngine) => {
    console.log(wEngine);
    setDataWEnigineEdit(wEngine);
    setShowModalEdit(true);
  };

  useEffect(() => {
    const handleStorageChange = (event) => {
      if (event.key === "selected wEngine") {
        setListSelectedAgents(event.newValue ? JSON.parse(event.newValue) : []);
      }
    };

    // Add event listener for storage event
    window.addEventListener("storage", handleStorageChange);

    // Clean up the event listener on component unmount
    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, []);

  const removeWEngine = (name) => {
    const updatedWEngines = listSelectedWEngines.filter(
      (wEngine) => wEngine.name !== name
    );
    setListSelectedWEngines(updatedWEngines);
    localStorage.setItem("selected wEngine", JSON.stringify(updatedWEngines));
    handleClose();
  };

  // Filter agents based on selectedOptions
  const filteredWEngines = listSelectedWEngines.filter((wEngine) => {
    return (
      (selectedOptions.rank === "all" ||
        !selectedOptions.rank ||
        wEngine.rank === selectedOptions.rank) &&
      (selectedOptions.fighting === "all" ||
        !selectedOptions.fighting ||
        wEngine.fightingStyle === selectedOptions.fighting)
    );
  });

  return (
    <div className="wEngine-grid">
      {filteredWEngines.map((item) => {
        return (
          <div
            className="card-container"
            key={item.name}
            onClick={() => handleEditWEngine(item)}
          >
            {/* Header */}
            <div
              className="card-header"
              onClick={() => handleEditWEngine(item)}
            >
              <div className={"card-icon rarity-" + item.rank}>
                <img src={item.nameIcon}></img>
              </div>
              <div className="card-info">
                <div className="card-title">{item.name}</div>
                <div className="card-rarity"></div>
                Rarity: {item.rank} | Type: Attack
              </div>
            </div>

            {/* Body */}
            {/* <div className="card-body">
              <p className="card-description">
                Increases <span className="ice-dmg">Ice DMG</span> by
                25/31.5/38/44.5/50%. Upon hitting an enemy with a Basic Attack,
                the equipper's CRIT Rate increases by 10/12.5/15/17.5/20% for
                8s. When dealing <span className="ice-dmg">Ice DMG</span> with a
                Dash Attack, the equipper's CRIT Rate increases by an additional
                10/12.5/15/17.5/20% for 15s. The duration of each effect is
                calculated separately.
              </p>
            </div> */}

            {/*Stat */}
            {/* <div className="card-stats">
              <div className="stat-level">
                <p>Level 1:</p>
                <p>Base ATK: 55</p>
                <p>Crit Rate: 9.6%</p>
              </div>
              <div className="stat-level">
                <p>Level 60:</p>
                <p>Base ATK: 713</p>
                <p>Crit Rate: 24%</p>
              </div>
            </div> */}
          </div>
        );
      })}
      <ModalEditWEngine
        show={isShowModalEdit}
        dataWEngineEdit={dataWEngineEdit}
        handleClose={handleClose}
        removeWEngine={removeWEngine}
      />
    </div>
  );
}

export default WEngineLocalDatabase;
