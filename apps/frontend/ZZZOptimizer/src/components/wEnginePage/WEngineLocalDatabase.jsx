import React from "react";
import "./wEngine.css";
import { useEffect, useState } from "react";

function WEngineLocalDatabase({
  listSelectedWEngines,
  setListSelectedWEngines,
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
    setDataAgentEdit(wEngine);
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
  return (
    <div className="wEngine-grid">
      {listSelectedWEngines.map((item) => {
        return (
          <div className="card-container" key={item.name}>
            {/* Header */}
            <div className="card-header">
              <img src={item.nameIcon}></img>
              <div className="card-title">{item.name}</div>
              <div className="card-rarity">
                Rarity: {item.rank} | Type: Attack
              </div>
            </div>

            {/* Body */}
            <div className="card-body">
              <p className="card-description">
                Increases <span className="ice-dmg">Ice DMG</span> by
                25/31.5/38/44.5/50%. Upon hitting an enemy with a Basic Attack,
                the equipper's CRIT Rate increases by 10/12.5/15/17.5/20% for
                8s. When dealing <span className="ice-dmg">Ice DMG</span> with a
                Dash Attack, the equipper's CRIT Rate increases by an additional
                10/12.5/15/17.5/20% for 15s. The duration of each effect is
                calculated separately.
              </p>
            </div>

            {/*Stat */}
            <div className="card-stats">
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
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default WEngineLocalDatabase;
