import React from "react";
import "./wEngine.css";
import { useEffect, useState } from "react";
import ModalEditWEngine from "./ModalEditWEngine";
import { getWEngineStats as fetchWEngineStats } from "../../services/WEngineService";

function WEngineLocalDatabase({
  listSelectedWEngines,
  setListSelectedWEngines,
  selectedOptions,
}) {
  // Init hashmap for SubStat display
  let subStatMap = new Map([
    ["hp", "HP"],
    ["hp_", "% HP"],
    ["atk", "Attack"],
    ["atk_", "% Attack"],
    ["def", "Defense"],
    ["def_", "% Defense"],
    ["impact", "Impact"],
    ["impact_", "% Impact"],
    ["critRate", "Crit Rate"],
    ["critRate_", "% Crit Rate"],
    ["critDMG", "Crit Damage"],
    ["critDMG_", "% Crit Damage"],
    ["anomalyMastery", "Anomaly Mastery"],
    ["anomalyMastery_", "% Anomaly Mastery"],
    ["anomalyProficiency", "Anomaly Proficiency"],
    ["anomalyProficiency_", "% Anomaly Proficiency"],
    ["pen", "Pen"],
    ["pen_", "Pen Ratio"],
    ["energyRegen", "Energy Regen"],
    ["energyRegen_", "% Energy Regen"],
    ["electricDMG_", "% Electric Damage"],
    ["physicalDMG_", "% Physical Damage"],
    ["fireDMG_", "% Fire Damage"],
    ["iceDMG_", "% Ice Damage"],
    ["etherDMG_", "% Ether Damage"],
  ]);

  // Init variable for wEngine edit show function
  const [isShowModalEdit, setShowModalEdit] = useState(false);
  const [dataWEngineEdit, setDataWEnigineEdit] = useState([]);

  // Closing function for ModalEditAgent
  const handleClose = () => {
    setShowModalEdit(false);
  };

  // Edit agent function
  const handleEditWEngine = (wEngine) => {
    setDataWEnigineEdit(wEngine);
    setSelectedLevel(wEngine.level);
    setSelectedUpgrade(wEngine.upgrade);
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
      (selectedOptions.specialty === "all" ||
        !selectedOptions.specialty ||
        wEngine.specialty === selectedOptions.specialty)
    );
  });

  // Set up data for ModalEditWEngine

  const [selectedLevel, setSelectedLevel] = useState(0);
  const [selectedUpgrade, setSelectedUpgrade] = useState("Select Upgrade");

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
                <div className="card-rarity">
                  Rarity: {item.rank} | Specialty: Attack
                </div>
                <div className="card-rarity">
                  Sub Stat: <b>{subStatMap.get(item.subStat[0])}</b>
                </div>
              </div>
            </div>
          </div>
        );
      })}
      <ModalEditWEngine
        show={isShowModalEdit}
        dataWEngineEdit={dataWEngineEdit}
        handleClose={handleClose}
        removeWEngine={removeWEngine}
        subStatMap={subStatMap}
        selectedLevel={selectedLevel}
        setSelectedLevel={setSelectedLevel}
        selectedUpgrade={selectedUpgrade}
        setSelectedUpgrade={setSelectedUpgrade}
      />
    </div>
  );
}

export default WEngineLocalDatabase;
