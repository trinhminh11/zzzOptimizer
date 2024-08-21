import React from "react";

import { useEffect, useState } from "react";

import "./agent.css";
import ModalEditAgent from "./ModalEditAgent";

export default function AgentLocalDatabase({
  listSelectedAgents,
  setListSelectedAgents,
  selectedOptions,
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

  // Filter agents based on selectedOptions
  const filteredAgents = listSelectedAgents.filter((agent) => {
    return (
      (selectedOptions.rank === "all" ||
        !selectedOptions.rank ||
        agent.rank === selectedOptions.rank) &&
      (selectedOptions.attribute === "all" ||
        !selectedOptions.attribute ||
        agent.attribute === selectedOptions.attribute) &&
      (selectedOptions.specialty === "all" ||
        !selectedOptions.specialty ||
        agent.specialty === selectedOptions.specialty)
    );
  });

  return (
    <div className="agent-local-database">
      <table>
        <thead>
          <tr>
            <th>Agent</th>
            <th className="center-column">Rank</th>
            <th className="attibute center-column">Attribute</th>
            <th className="specialty center-column">Specialty</th>
            <th className="faction center-column">Weapon</th>
            <th className="center-column">Mind Scape</th>
          </tr>
        </thead>
        <tbody>
          {filteredAgents.map((item) => {
            return (
              <tr key={`users-${item.name}`}>
                <td onClick={() => handleEditAgent(item)}>
                  <img src={item.nameIcon} alt="demo" className="agentImg" />
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
                  />
                </td>
                <td
                  className="center-column"
                  onClick={() => handleEditAgent(item)}
                >
                  <img src={item.attributeIcon} alt="demo" />
                </td>
                <td
                  className="center-column"
                  onClick={() => handleEditAgent(item)}
                >
                  <img src={item.specialtyIcon} alt="demo" />
                </td>
                <td onClick={() => handleEditAgent(item)}>Default weapon</td>
                <td className="center-column">
                  <span>M{item.mindScape}</span>
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
