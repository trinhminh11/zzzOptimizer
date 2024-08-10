import React from "react";

import { useEffect, useState } from "react";

import "./agent.css";
import ModalEditAgent from "./ModalEditAgent";

export default function AgentLocalDatabase({
  listSelectedAgents,
  setListSelectedAgents,
}) {
  // Init variable for agent edit show function
  const [isShowModalEdit, setShowModalEdit] = useState(false);
  const [dataAgentEdit, setDataAgentEdit] = useState([]);

  // Closing function for ModalEditAgent
  const handleClose = () => {
    setShowModalEdit(false);
  };

  // Edit agent function
  const handleEditAgent = (agent) => {
    console.log(agent);
    setDataAgentEdit(agent);
    setShowModalEdit(true);
  };

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
    handleClose();
  };

  return (
    <div className="agent-local-database">
      <table>
        <thead>
          <tr>
            <th>Agent</th>
            <th className="center-column">Rank</th>
            <th className="attibute center-column">Attribute</th>
            <th className="fighting-style center-column">Fighting Style</th>
            <th className="faction center-column">Weapon</th>
            <th className="center-column">Mind Scape</th>
          </tr>
        </thead>
        <tbody>
          {listSelectedAgents.map((item) => {
            return (
              <tr key={`users-${item.name}`}>
                <td onClick={() => handleEditAgent(item)}>
                  <img
                    src={item.nameIcon}
                    alt="demo"
                    className="agentImg"
                  ></img>
                  <span>{item.realName}</span>
                </td>
                <td
                  className="center-column"
                  onClick={() => handleEditAgent(item)}
                >
                  <img
                    src={item.rankIcon}
                    alt="demo"
                    style={{ width: "30px", height: "30px" }}
                  ></img>
                </td>
                <td
                  className="center-column"
                  onClick={() => handleEditAgent(item)}
                >
                  <img src={item.attributeIcon} alt="demo"></img>
                </td>
                <td
                  className="center-column"
                  onClick={() => handleEditAgent(item)}
                >
                  <img src={item.fightingStyleIcon} alt="demo"></img>
                </td>
                <td onClick={() => handleEditAgent(item)}>Default weapon</td>
                <td className="center-column">
                  <span> M{item.mindScape}</span>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <ModalEditAgent
        show={isShowModalEdit}
        dataAgentEdit={dataAgentEdit}
        handleClose={handleClose}
        removeAgent={removeAgent}
      />
    </div>
  );
}
