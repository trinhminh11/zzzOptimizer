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
      if (event.key === "agents") {
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
    localStorage.setItem("agents", JSON.stringify(updatedAgents));
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
          {filteredAgents.map((agent) => {
            return (
              <tr key={`users-${agent.name}`}>
                <td onClick={() => handleEditAgent(agent)}>
                  {/* <img src={agent.nameIcon} alt="demo" className="agentImg" /> */}
                  <img
                    src={
                      agent.api_dir + "media/agent/icon/" + agent.name + ".png"
                    }
                    alt="demo"
                    className="agentImg"
                  />
                  <span>{agent.realName}</span>
                </td>
                <td
                  className="center-column"
                  onClick={() => handleEditAgent(agent)}
                >
                  <img
                    src={agent.api_dir + "media/rank/" + agent.rank + ".png"}
                    alt="demo"
                    style={{ width: "30px", height: "30px" }}
                  />
                </td>
                <td
                  className="center-column"
                  onClick={() => handleEditAgent(agent)}
                >
                  <img
                    src={
                      agent.api_dir +
                      "media/attribute/" +
                      agent.attribute +
                      ".png"
                    }
                    alt="demo"
                  />
                </td>
                <td
                  className="center-column"
                  onClick={() => handleEditAgent(agent)}
                >
                  <img
                    src={
                      agent.api_dir +
                      "media/specialty/" +
                      agent.specialty +
                      ".png"
                    }
                    alt="demo"
                  />
                </td>
                <td onClick={() => handleEditAgent(agent)}>Default weapon</td>
                <td className="center-column">
                  <span>M{agent.mindScape}</span>
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
