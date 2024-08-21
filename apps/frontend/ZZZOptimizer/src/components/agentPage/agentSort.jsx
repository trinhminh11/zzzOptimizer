import React from "react";
import "./agent.css";
import fireIcon from "../../assets/icon/agentsAttributes/Icon_Fire.jpg";
import electricIcon from "../../assets/icon/agentsAttributes/Icon_Electric.jpg";
import etherIcon from "../../assets/icon/agentsAttributes/Icon_Ether.jpg";
import iceIcon from "../../assets/icon/agentsAttributes/Icon_Ice.jpg";
import physicalIcon from "../../assets/icon/agentsAttributes/Icon_Physical.jpg";
import sRankIcon from "../../assets/icon/agentsRanks/Icon_AgentRank_S.jpg";
import aRankIcon from "../../assets/icon/agentsRanks/Icon_AgentRank_A.jpg";
import attackIcon from "../../assets/icon/agentsRoles/Icon_Attack.jpg";
import anomalyIcon from "../../assets/icon/agentsRoles/Icon_Anomaly.jpg";
import defenseIcon from "../../assets/icon/agentsRoles/Icon_Defense.jpg";
import stunIcon from "../../assets/icon/agentsRoles/Icon_Stun.jpg";
import supportIcon from "../../assets/icon/agentsRoles/Icon_Support.jpg";
import { useState, useEffect } from "react";

export default function AgentSort({ selectedOptions, setSelectedOptions }) {
  const handleSelect = (category, option) => {
    setSelectedOptions((prevSelectedOptions) => ({
      ...prevSelectedOptions,
      [category]: prevSelectedOptions[category] === option ? null : option,
    }));
  };

  const isSelected = (category, option) => selectedOptions[category] === option;
  return (
    <div className=" agent-sorting-container">
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
      </div>

      {/* Element */}

      <div className="sorting-categories attribute-sort">
        <div
          className={`element-sort ${
            isSelected("attribute", "all") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "all")}
        >
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a
          className={`element-sort ${
            isSelected("attribute", "Electric") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Electric")}
        >
          <img alt="Electric Icon" src={electricIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("attribute", "Fire") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Fire")}
        >
          <img alt="Fire Icon" src={fireIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("attribute", "Physical") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Physical")}
        >
          <img alt="Physical Icon" src={physicalIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("attribute", "Ice") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Ice")}
        >
          <img alt="Ice Icon" src={iceIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("attribute", "Ether") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Ether")}
        >
          <img alt="Ether Icon" src={etherIcon} className="nav-icon" />
        </a>
      </div>

      {/* Specialty */}
      <div className="sorting-categories specialty-sort">
        <div
          className={`element-sort ${
            isSelected("specialty", "all") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "all")}
        >
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a
          className={`element-sort ${
            isSelected("specialty", "Attack") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Attack")}
        >
          <img alt="Attack Icon" src={attackIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("specialty", "Anomaly") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Anomaly")}
        >
          <img alt="Anomaly Icon" src={anomalyIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("specialty", "Defense") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Defense")}
        >
          <img alt="Defense Icon" src={defenseIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("specialty", "Stun") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Stun")}
        >
          <img alt="Stun Icon" src={stunIcon} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("specialty", "Support") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Support")}
        >
          <img alt="Support Icon" src={supportIcon} className="nav-icon" />
        </a>
      </div>
    </div>
  );
}
