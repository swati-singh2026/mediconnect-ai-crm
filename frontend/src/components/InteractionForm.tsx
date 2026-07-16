import React, { useState } from "react";

type Interaction = {
  doctorName: string;
  interactionType: string;
  date: string;
  notes: string;
};

export default function InteractionForm() {
  const [form, setForm] = useState<Interaction>({
    doctorName: "",
    interactionType: "",
    date: "",
    notes: "",
  });

  const handleChange = (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement
    >,
  ) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Saved interaction", form);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white p-6 rounded-lg shadow-md space-y-5"
    >
      <div>
        <label className="block mb-2 font-medium">Doctor Name</label>
        <input
          className="w-full border rounded-md p-2"
          name="doctorName"
          value={form.doctorName}
          onChange={handleChange}
          placeholder="Dr. Sharma"
        />
      </div>

      <div>
        <label className="block mb-2 font-medium">Interaction Type</label>
        <select
          className="w-full border rounded-md p-2"
          name="interactionType"
          value={form.interactionType}
          onChange={handleChange}
        >
          <option value="">Select...</option>
          <option value="call">Call</option>
          <option value="email">Email</option>
          <option value="visit">Visit</option>
        </select>
      </div>

      <div>
        <label className="block mb-2 font-medium">Date</label>
        <input
          className="w-full border rounded-md p-2"
          name="date"
          type="date"
          value={form.date}
          onChange={handleChange}
        />
      </div>

      <div>
        <label className="block mb-2 font-medium">Notes</label>
        <textarea
          className="w-full border rounded-md p-2 h-32"
          name="notes"
          value={form.notes}
          onChange={handleChange}
          placeholder="Enter interaction notes..."
        />
      </div>

      <button
        type="submit"
        className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
      >
        Save
      </button>
    </form>
  );
}
