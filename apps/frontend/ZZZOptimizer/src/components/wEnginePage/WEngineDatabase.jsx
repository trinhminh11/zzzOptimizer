import React, { useState, useEffect } from "react";
import "./wEngine.css";
import sRankIcon from "../../assets/icon/wEngineRanks/wEngine_Rank_S.jpg";
import aRankIcon from "../../assets/icon/wEngineRanks/wEngine_Rank_A.jpg";
import bRankIcon from "../../assets/icon/wEngineRanks/wEngine_Rank_B.jpg";
import attackIcon from "../../assets/icon/agentsRoles/Icon_Attack.jpg";
import anomalyIcon from "../../assets/icon/agentsRoles/Icon_Anomaly.jpg";
import defenseIcon from "../../assets/icon/agentsRoles/Icon_Defense.jpg";
import stunIcon from "../../assets/icon/agentsRoles/Icon_Stun.jpg";
import supportIcon from "../../assets/icon/agentsRoles/Icon_Support.jpg";

function WEngineDatabase({
  listWEngines,
  listSelectedWEngines,
  setListSelectedWEngines,
}) {
  // Initialize for search bar
  const [searchInput, setSearchInput] = useState("");
  const [selectedRank, setSelectedRank] = useState(null);
  const [selectedFightingStyle, setSelectedFightingStyle] = useState(null);

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

  const handleWEngineClick = (wEngine) => {
    const check = listSelectedWEngines.some(
      (selectedWEngine) => selectedWEngine.name === wEngine.name
    );
    if (!check) {
      const updatedWEngines = [...listSelectedWEngines, wEngine];
      setListSelectedWEngines(updatedWEngines);
      localStorage.setItem("selected wEngine", JSON.stringify(updatedWEngines));
    }
  };

  const handleRankClick = (rank) => {
    setSelectedRank((prev) => (prev === rank ? null : rank));
  };

  const handleFightingStyleClick = (style) => {
    setSelectedFightingStyle((prev) => (prev === style ? null : style));
  };

  // Filter wEngine based on search input and fighting style
  const filteredWEngines = listWEngines.filter((wEngine) => {
    const matchesSearch = wEngine.name
      .toLowerCase()
      .includes(searchInput.toLowerCase());
    const matchesFightingStyle = selectedFightingStyle
      ? wEngine.fightingStyle === selectedFightingStyle
      : true;
    return matchesSearch && matchesFightingStyle;
  });

  return (
    <div className="row left-table">
      <div className="search-bar">
        {/* Search Bar */}
        <input
          type="text"
          placeholder="Search an WEngine"
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        ></input>
      </div>

      {/* Fighting Style Fitler Bar */}
      <div className="filter-bar">
        <button
          type="button"
          className={`btn btn-secondary ${
            selectedFightingStyle === "Attack" ? "selected" : ""
          }`}
          onClick={() => handleFightingStyleClick("Attack")}
        >
          <img src={attackIcon} alt="attack icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedFightingStyle === "Anomaly" ? "selected" : ""
          }`}
          onClick={() => handleFightingStyleClick("Anomaly")}
        >
          <img src={anomalyIcon} alt="anomaly icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedFightingStyle === "Defense" ? "selected" : ""
          }`}
          onClick={() => handleFightingStyleClick("Defense")}
        >
          <img src={defenseIcon} alt="defense icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedFightingStyle === "Stun" ? "selected" : ""
          }`}
          onClick={() => handleFightingStyleClick("Stun")}
        >
          <img src={stunIcon} alt="stun icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedFightingStyle === "Support" ? "selected" : ""
          }`}
          onClick={() => handleFightingStyleClick("Support")}
        >
          <img src={supportIcon} alt="support icon" />
        </button>
      </div>

      {/* WEngine display */}
      <div className="agent-grid">
        {filteredWEngines.map((wEngine) => (
          <div
            className={"agent agent-" + wEngine.rank}
            key={wEngine.name}
            onClick={() => handleWEngineClick(wEngine)}
          >
            <img src={wEngine.nameIcon} alt="demo"></img>
            <div className="agent-name-showcase">{wEngine.name} </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default WEngineDatabase;
