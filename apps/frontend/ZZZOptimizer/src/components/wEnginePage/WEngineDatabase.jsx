import React, { useState, useEffect } from "react";
import "./wEngine.css";
import util from "../../util"

function WEngineDatabase({
  listWEngines,
  listSelectedWEngines,
  setListSelectedWEngines,
}) {
  // Initialize for search bar
  const [searchInput, setSearchInput] = useState("");
  const [selectedRank, setSelectedRank] = useState(null);
  const [selectedSpecialty, setSelectedSpecialty] = useState(null);

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

  const handleWEngineClick = (wEngine) => {
    // Clone the wEngine and give it a new unique ID
    const wEngineWithUniqueID = {
      ...wEngine,
      id: `wEngine-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
    };

    // Add the cloned item to the list
    const updatedWEngines = [...listSelectedWEngines, wEngineWithUniqueID];
    setListSelectedWEngines(updatedWEngines);

    // Update the localStorage with the new list
    localStorage.setItem("wengines", JSON.stringify(updatedWEngines));

  };

  const handleSpecialtyClick = (style) => {
    setSelectedSpecialty((prev) => (prev === style ? null : style));
  };

  // Filter wEngine based on search input and specialty
  const filteredWEngines = listWEngines.filter((wEngine) => {
    const matchesSearch = wEngine.name
      .toLowerCase()
      .includes(searchInput.toLowerCase());
    const matchesSpecialty = selectedSpecialty
      ? wEngine.specialty === selectedSpecialty
      : true;
    return matchesSearch && matchesSpecialty;
  });

  return (
    <div className="row left-table">
      <div className="search-bar">
        {/* Search Bar */}
        <input
          type="text"
          placeholder="Search a WEngine"
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        ></input>
      </div>

      {/* Specialty Fitler Bar */}
      <div className="filter-bar">
        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Attack" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Attack")}
        >
          <img src={util.specialtyIcon.attack} alt="attack icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Anomaly" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Anomaly")}
        >
          <img src={util.specialtyIcon.anomaly} alt="anomaly icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Defense" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Defense")}
        >
          <img src={util.specialtyIcon.defense} alt="defense icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Stun" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Stun")}
        >
          <img src={util.specialtyIcon.stun} alt="stun icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Support" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Support")}
        >
          <img src={util.specialtyIcon.support} alt="support icon" />
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
            <img src={util.api_dir + "media/wengine/icon/" + util.trim(wEngine.name.replaceAll(/[^0-9a-zA-Z]+/gm, "_"), "_") + ".png"} alt="demo"></img>
            <div className="agent-name-showcase">{wEngine.name} </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default WEngineDatabase;
