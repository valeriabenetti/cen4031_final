import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import Tickets from './components/Tickets';
import CreateTicketForm from './components/CreateTicketForm';


const App = () => {
  const [isCreating, setIsCreating] = useState(false);

  const handleSave = (newTicket) => {
    // Save ticket to the backend
    fetch('/api/tickets', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newTicket),
    }).then(() => {
      setIsCreating(false);
      // Optionally, refetch the tickets list or update the state
    });
  };

  return (
    <div>
      <Tickets />
      <button onClick={() => setIsCreating(true)}>Create Ticket</button>
      {isCreating && <CreateTicketForm onSave={handleSave} />}
    </div>
  );
};


export default App;
