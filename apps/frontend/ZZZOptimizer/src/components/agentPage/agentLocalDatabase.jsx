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
  const [agents, setAgents] = useState([]);
  useEffect(() => {
    storedAgent();
  }, []);

  const storedAgent = async () => {
    let res = await localStorage.getItem("selectedAgent");
    if (res) {
      setAgents(JSON.parse(res));
    }
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
          {/* <tr>
            <td>
              <img alt="Rina Icon" src={agentRinaIcon} className="nav-icon" />
            </td>
            <td>Alexandrina Sebastiane</td>
            <td>
              <img src={sRankIcon} alt="S Rank"></img>
            </td>
            <td>
              <img
                alt="Electric Icon"
                src={electricIcon}
                className="nav-icon"
              />
              <span>Electric</span>
            </td>
            <td>
              <img src={supportRole} alt="Support"></img>
              <span>Support</span>
            </td>
            <td>
              <img src={victoriaFacton} alt="Victoria"></img>
              <span>Victoria Housekeeping</span>
            </td>
            <td>
              <button>Remove</button>
            </td>
          </tr> */}
          {console.log(agents)}
          {agents &&
            agents.length > 0 &&
            agents.map((item) => {
              return (
                <tr key={`users-${item.characterName}`}>
                  <td>
                    <img src={item.icon} alt="demo"></img>
                  </td>
                  <td>{item.characterName}</td>
                  <td>{item.rank}</td>
                  <td>{item.attribute}</td>
                  <td>{item.style}</td>
                  <td>{item.faction}</td>
                  <td>
                    <button className="btn btn-danger">Delete</button>
                  </td>
                </tr>
              );
            })}
        </tbody>
      </table>
    </div>
  );
}
