import React, { useState, useEffect } from 'react';


const Tickets = () => {
  const [tickets, setTickets] = useState([]);

  // Fetch tickets from the backend API
  useEffect(() => {
    fetch('/api/tickets')
      .then(response => response.json())
      .then(data => setTickets(data));
  }, []);

  return (
    <div>
      <h1>Help Desk Tickets</h1>
      {tickets.length === 0 ? (
        <p>No tickets available</p>
      ) : (
        <ul>
          {tickets.map(ticket => (
            <li key={ticket.id}>
              <strong>{ticket.name}</strong> - {ticket.date} - {ticket.problemDescription}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Tickets;
