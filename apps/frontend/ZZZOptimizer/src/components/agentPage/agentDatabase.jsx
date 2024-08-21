import React, { useState, useEffect } from "react";
import fireIcon from "../../assets/icon/agentsAttributes/Icon_Fire.jpg";
import electricIcon from "../../assets/icon/agentsAttributes/Icon_Electric.jpg";
import etherIcon from "../../assets/icon/agentsAttributes/Icon_Ether.jpg";
import iceIcon from "../../assets/icon/agentsAttributes/Icon_Ice.jpg";
import physicalIcon from "../../assets/icon/agentsAttributes/Icon_Physical.jpg";
import attackIcon from "../../assets/icon/agentsRoles/Icon_Attack.jpg";
import anomalyIcon from "../../assets/icon/agentsRoles/Icon_Anomaly.jpg";
import defenseIcon from "../../assets/icon/agentsRoles/Icon_Defense.jpg";
import stunIcon from "../../assets/icon/agentsRoles/Icon_Stun.jpg";
import supportIcon from "../../assets/icon/agentsRoles/Icon_Support.jpg";

import "./agent.css";

function AgentDatabase({
  listAgents,
  listSelectedAgents,
  setListSelectedAgents,
}) {
  // Initialize for search bar
  const [searchInput, setSearchInput] = useState("");
  const [selectedAttribute, setSelectedAttribute] = useState(null);
  const [selectedSpecialty, setSelectedSpecialty] = useState(null);

  useEffect(() => {
    const handleStorageChange = (event) => {
      if (event.key === "selected agent") {
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

  const handleAgentClick = (agent) => {
    const check = listSelectedAgents.some(
      (selectedAgent) => selectedAgent.name === agent.name
    );

    if (!check) {
      const updatedAgents = [...listSelectedAgents, agent];
      console.log(updatedAgents);
      setListSelectedAgents(updatedAgents);
      localStorage.setItem("selected agent", JSON.stringify(updatedAgents));
    }
  };

  const handleAttributeClick = (attribute) => {
    setSelectedAttribute((prev) => (prev === attribute ? null : attribute));
  };

  const handleSpecialtyClick = (style) => {
    setSelectedSpecialty((prev) => (prev === style ? null : style));
  };

  // // Filter agents based on search input
  // const filteredAgents = listAgents.filter((agent) =>
  //   agent.name.toLowerCase().includes(searchInput.toLowerCase())
  // );

  // Filter agents based on search input, selected attribute, and specialty
  const filteredAgents = listAgents.filter((agent) => {
    const matchesSearch = agent.name
      .toLowerCase()
      .includes(searchInput.toLowerCase());
    const matchesAttribute = selectedAttribute
      ? agent.attribute === selectedAttribute
      : true;
    const matchesSpecialty = selectedSpecialty
      ? agent.specialty === selectedSpecialty
      : true;
    return matchesSearch && matchesAttribute && matchesSpecialty;
  });

  return (
    <div className="row left-table">
      {/* Search Bar  */}
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search an agent"
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        ></input>
      </div>

      {/* Attribute Filter Bar  */}
      <div className="filter-bar">
        {/* Elements */}
        <button
          type="button"
          className={`btn btn-secondary ${
            selectedAttribute === "Electric" ? "selected" : ""
          }`}
          onClick={() => handleAttributeClick("Electric")}
        >
          <img alt="Electric Icon" src={electricIcon} className="nav-icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedAttribute === "Fire" ? "selected" : ""
          }`}
          onClick={() => handleAttributeClick("Fire")}
        >
          <img alt="Fire Icon" src={fireIcon} className="nav-icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedAttribute === "Physical" ? "selected" : ""
          }`}
          onClick={() => handleAttributeClick("Physical")}
        >
          <img alt="Physical Icon" src={physicalIcon} className="nav-icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedAttribute === "Ice" ? "selected" : ""
          }`}
          onClick={() => handleAttributeClick("Ice")}
        >
          <img alt="Ice Icon" src={iceIcon} className="nav-icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedAttribute === "Ether" ? "selected" : ""
          }`}
          onClick={() => handleAttributeClick("Ether")}
        >
          <img alt="Ether Icon" src={etherIcon} className="nav-icon" />
        </button>
      </div>

      {/* Specialty Filter Bar  */}
      <div className="filter-bar">
        {/* Elements */}
        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Anomaly" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Anomaly")}
        >
          <img alt="Anomaly Icon" src={anomalyIcon} className="nav-icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Attack" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Attack")}
        >
          <img alt="Attack Icon" src={attackIcon} className="nav-icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Defense" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Defense")}
        >
          <img alt="Defense Icon" src={defenseIcon} className="nav-icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Stun" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Stun")}
        >
          <img alt="Stun Icon" src={stunIcon} className="nav-icon" />
        </button>

        <button
          type="button"
          className={`btn btn-secondary ${
            selectedSpecialty === "Support" ? "selected" : ""
          }`}
          onClick={() => handleSpecialtyClick("Support")}
        >
          <img alt="Support Icon" src={supportIcon} className="nav-icon" />
        </button>
      </div>

      {/* Champion display */}
      <div className="agent-grid">
        {filteredAgents.map((agent) => (
          <div
            className={"agent agent-" + agent.rank}
            key={agent.id}
            onClick={() => handleAgentClick(agent)}
          >
            <img src={agent.nameIcon} alt="demo"></img>
            <div className="agent-name-showcase">{agent.name} </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AgentDatabase;
