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
import { AgentsService } from "../../services/AgentService";
import "./agent.css";

function AgentDatabase() {
  // set up list for store agent from api
  const [listAgents, setListAgents] = useState([]);

  // set up localstorage to store infomation
  const [listSelectedAgents, setListSelectedAgents] = useState(() => {
    // Check local storage and initialize list
    const storedAgents = localStorage.getItem("selected agent");
    return storedAgents ? JSON.parse(storedAgents) : [];
  });

  // Set up function to store data from api into the list
  useEffect(() => {
    getAgents();
  }, []);

  const getAgents = async () => {
    let res = await AgentsService();
    if (res) {
      setListAgents(res);
    }
  };

  // useEffect(() => {
  //   const handleStorageChange = (event) => {
  //     if (event.key === "selected agent") {
  //       setListSelectedAgents(event.newValue ? JSON.parse(event.newValue) : []);
  //     }
  //   };

  //   // Add event listener for storage event
  //   window.addEventListener("storage", handleStorageChange);

  //   // Clean up the event listener on component unmount
  //   return () => {
  //     window.removeEventListener("storage", handleStorageChange);
  //   };
  // }, []);

  const handleAgentClick = (agent) => {
    const check = listSelectedAgents.some(
      (selectedAgent) => selectedAgent.name === agent.name
    );

    if (!check) {
      const updatedAgents = [...listSelectedAgents, agent];
      setListSelectedAgents(updatedAgents);
      localStorage.setItem("selected agent", JSON.stringify(updatedAgents));
      location.reload();
    }
  };

  return (
    <div className="row left-table">
      {/* Search Bar  */}
      <div className="search-bar">
        <input type="text" placeholder="Search an agent"></input>
      </div>

      {/* Attribute Filter Bar  */}
      <div className="filter-bar">
        {/* Elements */}
        <button type="button" className="btn btn-secondary">
          <img alt="Electric Icon" src={electricIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Fire Icon" src={fireIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Physical Icon" src={physicalIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Ice Icon" src={iceIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Ether Icon" src={etherIcon} className="nav-icon" />
        </button>
      </div>

      {/* Fighting style Filter Bar  */}
      <div className="filter-bar">
        {/* Elements */}
        <button type="button" className="btn btn-secondary">
          <img alt="Anomaly Icon" src={anomalyIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Attack Icon" src={attackIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Defense Icon" src={defenseIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Stun Icon" src={stunIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Support Icon" src={supportIcon} className="nav-icon" />
        </button>
      </div>

      {/* Champion display */}
      <div className="agent-grid">
        {listAgents.map((agent) => (
          <div
            className="agent"
            key={agent.id}
            onClick={() => handleAgentClick(agent)}
          >
            <img src={agent.icon} alt="demo"></img>
            <div className="agent-name-showcase">{agent.name} </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AgentDatabase;
