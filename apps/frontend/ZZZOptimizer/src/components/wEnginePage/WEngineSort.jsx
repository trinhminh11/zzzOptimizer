import React from "react";
import sRankIcon from "../../assets/icon/wEngineRanks/wEngine_Rank_S.jpg";
import aRankIcon from "../../assets/icon/wEngineRanks/wEngine_Rank_A.jpg";
import bRankIcon from "../../assets/icon/wEngineRanks/wEngine_Rank_B.jpg";
import attackIcon from "../../assets/icon/agentsRoles/Icon_Attack.jpg";
import anomalyIcon from "../../assets/icon/agentsRoles/Icon_Anomaly.jpg";
import defenseIcon from "../../assets/icon/agentsRoles/Icon_Defense.jpg";
import stunIcon from "../../assets/icon/agentsRoles/Icon_Stun.jpg";
import supportIcon from "../../assets/icon/agentsRoles/Icon_Support.jpg";
import "./wEngine.css";

function WEngineSort({ selectedOptions, setSelectedOptions }) {
  const handleSelect = (category, option) => {
    setSelectedOptions((prevSelectedOptions) => ({
      ...prevSelectedOptions,
      [category]: prevSelectedOptions[category] === option ? null : option,
    }));
  };

  const isSelected = (category, option) => selectedOptions[category] === option;
  return (
    <div className="wEngine-sorting-container">
      {/* Search Bar */}
      <div className="top-search-bar">
        <input
          type="text"
          placeholder="Search an WEngine"
          // value={searchInput}
          // onChange={(e) => setSearchInput(e.target.value)}
          className="search-input"
        ></input>
      </div>

      {/* Rank  */}
      <div className="sorting-categories rank-sort">
        <div
          className={`element-sort ${
            isSelected("rank", "all") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "all")}
        >
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a
          className={`element-sort ${
            isSelected("rank", "S") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "S")}
        >
          <img alt="S rank Icon" src={sRankIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("rank", "A") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "A")}
        >
          <img alt="A rank Icon" src={aRankIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("rank", "B") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "B")}
        >
          <img alt="B rank Icon" src={bRankIcon} className="nav-icon" />
        </a>
      </div>

      {/* Fighting Style */}
      <div className="sorting-categories fighting-sort">
        <div
          className={`element-sort ${
            isSelected("fighting", "all") ? "selected" : ""
          }`}
          onClick={() => handleSelect("fighting", "all")}
        >
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a
          className={`element-sort ${
            isSelected("fighting", "Attack") ? "selected" : ""
          }`}
          onClick={() => handleSelect("fighting", "Attack")}
        >
          <img alt="Attack Icon" src={attackIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("fighting", "Anomaly") ? "selected" : ""
          }`}
          onClick={() => handleSelect("fighting", "Anomaly")}
        >
          <img alt="Anomaly Icon" src={anomalyIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("fighting", "Defense") ? "selected" : ""
          }`}
          onClick={() => handleSelect("fighting", "Defense")}
        >
          <img alt="Defense Icon" src={defenseIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("fighting", "Stun") ? "selected" : ""
          }`}
          onClick={() => handleSelect("fighting", "Stun")}
        >
          <img alt="Stun Icon" src={stunIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("fighting", "Support") ? "selected" : ""
          }`}
          onClick={() => handleSelect("fighting", "Support")}
        >
          <img alt="Support Icon" src={supportIcon} className="nav-icon" />
        </a>
      </div>
    </div>
  );
}

export default WEngineSort;
