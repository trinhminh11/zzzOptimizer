import React from "react";
import "./agent.css";

import util from "../../util";

export default function AgentSelect({ selectedOptions, setSelectedOptions }) {
  const handleSelect = (category, option) => {
    setSelectedOptions((prevSelectedOptions) => ({
      ...prevSelectedOptions,
      [category]: prevSelectedOptions[category] === option ? null : option,
    }));
  };

  const isSelected = (category, option) => selectedOptions[category] === option;
  return (
    <div className=" agent-selecting-container">
      {/* Rank  */}
      <div className="selecting-categories rank-select">
        <div
          className={`element-select ${
            isSelected("rank", "all") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "all")}
        >
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a
          className={`element-select ${
            isSelected("rank", "S") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "S")}
        >
          <img alt="S rank Icon" src={util.agentRankIcon.S} className="nav-icon" />
        </a>

        <a
          className={`element-select ${
            isSelected("rank", "A") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "A")}
        >
          <img alt="A rank Icon" src={util.agentRankIcon.A} className="nav-icon" />
        </a>
      </div>

      {/* Element */}

      <div className="selecting-categories attribute-select">
        <div
          className={`element-select ${
            isSelected("attribute", "all") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "all")}
        >
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a
          className={`element-select ${
            isSelected("attribute", "Electric") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Electric")}
        >
          <img alt="Electric Icon" src={util.attributeIcon.electric} className="nav-icon" />
        </a>

        <a
          className={`element-select ${
            isSelected("attribute", "Fire") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Fire")}
        >
          <img alt="Fire Icon" src={util.attributeIcon.fire} className="nav-icon" />
        </a>

        <a
          className={`element-select ${
            isSelected("attribute", "Physical") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Physical")}
        >
          <img alt="Physical Icon" src={util.attributeIcon.physical} className="nav-icon" />
        </a>

        <a
          className={`element-select ${
            isSelected("attribute", "Ice") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Ice")}
        >
          <img alt="Ice Icon" src={util.attributeIcon.ice} className="nav-icon" />
        </a>

        <a
          className={`element-select ${
            isSelected("attribute", "Ether") ? "selected" : ""
          }`}
          onClick={() => handleSelect("attribute", "Ether")}
        >
          <img alt="Ether Icon" src={util.attributeIcon.ether} className="nav-icon" />
        </a>
      </div>

      {/* Specialty */}
      <div className="selecting-categories specialty-select">
        <div
          className={`element-select ${
            isSelected("specialty", "all") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "all")}
        >
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a
          className={`element-select ${
            isSelected("specialty", "Attack") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Attack")}
        >
          <img alt="Attack Icon" src={util.specialtyIcon.attack} className="nav-icon" />
        </a>

        <a
          className={`element-select ${
            isSelected("specialty", "Anomaly") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Anomaly")}
        >
          <img alt="Anomaly Icon" src={util.specialtyIcon.anomaly} className="nav-icon" />
        </a>

        <a
          className={`element-select ${
            isSelected("specialty", "Defense") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Defense")}
        >
          <img alt="Defense Icon" src={util.specialtyIcon.defense} className="nav-icon" />
        </a>

        <a
          className={`element-select ${
            isSelected("specialty", "Stun") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Stun")}
        >
          <img alt="Stun Icon" src={util.specialtyIcon.stun} className="nav-icon" />
        </a>

        <a
          className={`element-select ${
            isSelected("specialty", "Support") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Support")}
        >
          <img alt="Support Icon" src={util.specialtyIcon.support} className="nav-icon" />
        </a>
      </div>
    </div>
  );
}
