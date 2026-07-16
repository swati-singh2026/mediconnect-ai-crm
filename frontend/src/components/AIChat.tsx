import { useState } from "react";

const AIChat = () => {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    console.log("Send:", message);
    setMessage("");
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-xl font-semibold mb-4">AI Chat</h2>

      <textarea
        className="w-full border rounded-md p-3 h-40 focus:outline-none focus:ring-2 focus:ring-blue-500"
        placeholder="I met Dr. Sharma today..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button
        onClick={handleSend}
        className="mt-4 bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
      >
        Send
      </button>
    </div>
  );
};

export default AIChat;
