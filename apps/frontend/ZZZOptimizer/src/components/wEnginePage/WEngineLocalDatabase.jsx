import React from "react";
import "./wEngine.css";
import { useEffect, useState } from "react";
import ModalEditWEngine from "./ModalEditWEngine";
import { getWEngineStats as fetchWEngineStats } from "../../services/WEngineService";

import util from "../../util";

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

  // Edit wEngine function
  const handleEditWEngine = (wEngine) => {
    setDataWEnigineEdit(wEngine);
    setSelectedLevel(wEngine.level);
    setSelectedUpgrade(wEngine.upgrade);
    setSelectedModification(wEngine.modification);
    setModificationDisplay((Math.floor(wEngine.level / 10) + 1) * 10);
    setShowModalEdit(true);
  };

  useEffect(() => {
    const handleStorageChange = (event) => {
      if (event.key === "wengines") {
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
    localStorage.setItem("wengines", JSON.stringify(updatedWEngines));
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
  const [selectedUpgrade, setSelectedUpgrade] = useState(1);
  const [selectedModification, setSelectedModification] = useState(0);
  const [modificationDisplay, setModificationDisplay] = useState(
    (Math.floor(selectedLevel / 10) + 1) * 10
  );

  return (
    <div className="wEngine-grid">
      {filteredWEngines.map((wEngine) => {
        return (
          <div
            className="card-container"
            key={wEngine.id}
            onClick={() => handleEditWEngine(wEngine)}
          >
            {/* Header */}
            <div
              className="card-header"
              onClick={() => handleEditWEngine(wEngine)}
            >
              <div className={"card-icon rarity-" + wEngine.rank}>
                <img
                  src={
                    util.api_dir +
                    "media/wengine/icon/" +
                    util.trim(
                      wEngine.name.replaceAll(/[^0-9a-zA-Z]+/gm, "_"),
                      "_"
                    ) +
                    ".png"
                  }
                ></img>
              </div>
              <div className="card-info">
                <div className="card-title">{wEngine.name}</div>
                <div className="card-rarity">
                  Rarity: {wEngine.rank} | Specialty: Attack
                </div>
                <div className="card-rarity">
                  Sub Stat: <b>{subStatMap.get(wEngine.subStat[0])}</b> | Lv:{" "}
                  {wEngine.level}
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
        selectedModification={selectedModification}
        setSelectedModification={setSelectedModification}
        modificationDisplay={modificationDisplay}
        setModificationDisplay={setModificationDisplay}
      />
    </div>
  );
}

export default WEngineLocalDatabase;
