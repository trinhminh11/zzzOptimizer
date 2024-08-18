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

function WEngineSort() {
  return (
    <div className="wEngine-sorting-container">
      {/* Rank  */}
      <div className="sorting-categories rank-sort">
        <div
          //   className={`element-sort ${
          //     isSelected("rank", "all") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("rank", "all")}
          className="element-sort"
        >
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a
          //   className={`element-sort ${
          //     isSelected("rank", "S") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("rank", "S")}
          className="element-sort"
        >
          <img alt="S rank Icon" src={sRankIcon} className="nav-icon" />
        </a>

        <a
          //   className={`element-sort ${
          //     isSelected("rank", "A") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("rank", "A")}
          className="element-sort"
        >
          <img alt="A rank Icon" src={aRankIcon} className="nav-icon" />
        </a>

        <a
          //   className={`element-sort ${
          //     isSelected("rank", "A") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("rank", "A")}
          className="element-sort"
        >
          <img alt="A rank Icon" src={bRankIcon} className="nav-icon" />
        </a>
      </div>

      {/* Fighting Style */}
      <div className="sorting-categories fighting-sort">
        <div
          //   className={`element-sort ${
          //     isSelected("fighting", "all") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("fighting", "all")}
          className="element-sort"
        >
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a
          //   className={`element-sort ${
          //     isSelected("fighting", "Attack") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("fighting", "Attack")}
          className="element-sort"
        >
          <img alt="Attack Icon" src={attackIcon} className="nav-icon" />
        </a>

        <a
          //   className={`element-sort ${
          //     isSelected("fighting", "Anomaly") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("fighting", "Anomaly")}
          className="element-sort"
        >
          <img alt="Anomaly Icon" src={anomalyIcon} className="nav-icon" />
        </a>

        <a
          //   className={`element-sort ${
          //     isSelected("fighting", "Defense") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("fighting", "Defense")}
          className="element-sort"
        >
          <img alt="Defense Icon" src={defenseIcon} className="nav-icon" />
        </a>

        <a
          //   className={`element-sort ${
          //     isSelected("fighting", "Stun") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("fighting", "Stun")}
          className="element-sort"
        >
          <img alt="Stun Icon" src={stunIcon} className="nav-icon" />
        </a>

        <a
          //   className={`element-sort ${
          //     isSelected("fighting", "Support") ? "selected" : ""
          //   }`}
          //   onClick={() => handleSelect("fighting", "Support")}
          className="element-sort"
        >
          <img alt="Support Icon" src={supportIcon} className="nav-icon" />
        </a>
      </div>
    </div>
  );
}

export default WEngineSort;
