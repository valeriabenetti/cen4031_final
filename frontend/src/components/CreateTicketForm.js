import React, { useState } from 'react';

const CreateTicketForm = ({ onSave }) => {
  const [name, setName] = useState('');
  const [date, setDate] = useState('');
  const [problemDescription, setProblemDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const newTicket = { name, date, problemDescription };
    onSave(newTicket);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
      </div>
      <div>
        <label>Date</label>
        <input type="date" value={date} onChange={(e) => setDate(e.target.value)} required />
      </div>
      <div>
        <label>Problem Description</label>
        <textarea value={problemDescription} onChange={(e) => setProblemDescription(e.target.value)} required />
      </div>
      <button type="submit">Save Ticket</button>
    </form>
  );
};

export default CreateTicketForm;