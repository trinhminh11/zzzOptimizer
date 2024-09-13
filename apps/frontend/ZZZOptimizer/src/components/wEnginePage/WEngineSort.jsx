import React from "react";
import "./wEngine.css";
import util from "../../util";

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
          placeholder="Search a WEngine"
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
          <i className="bi bi-asterisk select-all"></i>
        </div>

        <a
          className={`element-sort ${
            isSelected("rank", "S") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "S")}
        >
          <img alt="S rank Icon" src={util.wEngineRankIcon.S} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("rank", "A") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "A")}
        >
          <img alt="A rank Icon" src={util.wEngineRankIcon.A} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("rank", "B") ? "selected" : ""
          }`}
          onClick={() => handleSelect("rank", "B")}
        >
          <img alt="B rank Icon" src={util.wEngineRankIcon.B} className="nav-icon" />
        </a>
      </div>

      {/* Fighting Style */}
      <div className="sorting-categories specialty-sort">
        <div
          className={`element-sort ${
            isSelected("specialty", "all") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "all")}
        >
          <i className="bi bi-asterisk select-all"></i>
        </div>

        <a
          className={`element-sort ${
            isSelected("specialty", "Attack") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Attack")}
        >
          <img alt="Attack Icon" src={util.specialtyIcon.attack} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("specialty", "Anomaly") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Anomaly")}
        >
          <img alt="Anomaly Icon" src={util.specialtyIcon.anomaly} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("specialty", "Defense") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Defense")}
        >
          <img alt="Defense Icon" src={util.specialtyIcon.defense} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
            isSelected("specialty", "Stun") ? "selected" : ""
          }`}
          onClick={() => handleSelect("specialty", "Stun")}
        >
          <img alt="Stun Icon" src={util.specialtyIcon.stun} className="nav-icon" />
        </a>

        <a
          className={`element-sort ${
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

export default WEngineSort;
