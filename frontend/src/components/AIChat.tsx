import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import type { RootState } from "../store/store";
import { setCurrentChat } from "../features/interaction/interactionSlice";

const AIChat = () => {
  const [message, setMessage] = useState("");

  const dispatch = useDispatch();

  const currentChat = useSelector(
    (state: RootState) => state.interaction.currentChat,
  );

  const handleSend = () => {
    if (!message.trim()) return;

    dispatch(setCurrentChat(message));

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

      {/* Redux State Preview */}
      <div className="mt-6 border-t pt-4">
        <h3 className="font-semibold text-gray-700">Current Chat</h3>
        <p className="mt-2 text-gray-600">
          {currentChat || "No chat sent yet."}
        </p>
      </div>
    </div>
  );
};

export default AIChat;
