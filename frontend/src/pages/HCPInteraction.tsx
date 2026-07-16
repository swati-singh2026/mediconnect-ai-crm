import { useState } from "react";
import Header from "../components/Header";
import InteractionForm from "../components/InteractionForm";
import AIChat from "../components/AIChat";

const HCPInteraction = () => {
  const [activeTab, setActiveTab] = useState("form");

  return (
    <div className="min-h-screen bg-gray-100">
      <Header />

      <main className="max-w-4xl mx-auto p-6">
        <h2 className="text-3xl font-bold mb-6">HCP Interaction</h2>

        {/* Tabs */}
        <div className="flex border-b mb-6">
          <button
            className={`px-6 py-2 ${
              activeTab === "form"
                ? "border-b-2 border-blue-600 font-semibold"
                : "text-gray-500"
            }`}
            onClick={() => setActiveTab("form")}
          >
            Structured Form
          </button>

          <button
            className={`px-6 py-2 ${
              activeTab === "chat"
                ? "border-b-2 border-blue-600 font-semibold"
                : "text-gray-500"
            }`}
            onClick={() => setActiveTab("chat")}
          >
            AI Chat
          </button>
        </div>

        {activeTab === "form" ? <InteractionForm /> : <AIChat />}
      </main>
    </div>
  );
};

export default HCPInteraction;
