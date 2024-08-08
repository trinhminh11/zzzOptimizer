import React from "react";
import fireIcon from "../../assets/icon/agentsAttributes/Icon_Fire.jpg";
import electricIcon from "../../assets/icon/agentsAttributes/Icon_Electric.jpg";
import etherIcon from "../../assets/icon/agentsAttributes/Icon_Ether.jpg";
import iceIcon from "../../assets/icon/agentsAttributes/Icon_Ice.jpg";
import physicalIcon from "../../assets/icon/agentsAttributes/Icon_Physical.jpg";
import agentRinaIcon from "../../assets/icon/agents/Rina.jpg";
import sRankIcon from "../../assets/icon/agentsRanks/Icon_AgentRank_S.jpg";
import aRankIcon from "../../assets/icon/agentsRanks/Icon_AgentRank_A.jpg";
import anomalyRole from "../../assets/icon/agentsRoles/Icon_Anomaly.jpg";
import attackRole from "../../assets/icon/agentsRoles/Icon_Attack.jpg";
import supportRole from "../../assets/icon/agentsRoles/Icon_Support.jpg";
import victoriaFacton from "../../assets/icon/agentFactions/Victoria_Housekeeping_Icon.jpg";
import { useEffect, useState } from "react";

import "./agent.css";

export default function AgentLocalDatabase() {
  // // List to store selected agents

  // var listSelectedAgents = [];

  // // Check null and initialize list
  // if (localStorage.getItem("selected agent") == null) {
  //   listSelectedAgents = [];
  // } else {
  //   listSelectedAgents = JSON.parse(localStorage.getItem("selected agent"));
  // }

  const [listSelectedAgents, setListSelectedAgents] = useState(() => {
    // Check local storage and initialize list
    const storedAgents = localStorage.getItem("selected agent");
    return storedAgents ? JSON.parse(storedAgents) : [];
  });

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

  const removeAgent = (name) => {
    const updatedAgents = listSelectedAgents.filter(
      (agent) => agent.name !== name
    );
    setListSelectedAgents(updatedAgents);
    localStorage.setItem("selected agent", JSON.stringify(updatedAgents));
  };

  return (
    <div className="agent-local-database">
      <table>
        <thead>
          <tr>
            <th>Icon</th>
            <th>Name</th>
            <th>Rank</th>
            <th className="attibute">Attribute</th>
            <th className="fighting-style">Fighting Style</th>
            <th className="faction">Faction</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {listSelectedAgents.map((item) => {
            return (
              <tr key={`users-${item.name}`}>
                <td>
                  <img src={item.icon} alt="demo"></img>
                </td>
                <td>{item.realName}</td>
                <td>{item.rank}</td>
                {/* <td>{item.attribute}</td> */}
                <td>TBD</td>
                <td>{item.fightingStyle}</td>
                <td>{item.faction}</td>
                <td>
                  <button
                    className="btn btn-danger"
                    onClick={() => removeAgent(item.name)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
