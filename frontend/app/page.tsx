'use client';

import { useState, useEffect } from 'react';

export default function Home() {
  const [clues, setClues] = useState<string[]>([]);
  const [countryId, setCountryId] = useState('');
  const [guess, setGuess] = useState('');
  const [result, setResult] = useState('');
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);

  const fetchCountry = async () => {
    setResult('');
    setGuess('');
    setIsCorrect(null);
    const res = await fetch('http://127.0.0.1:5000/api/country');
    const data = await res.json();
    setClues(data.clues);
    setCountryId(data.id);
  };

  useEffect(() => {
    fetchCountry();
  }, []);

  const submitGuess = async () => {
    const res = await fetch('http://127.0.0.1:5000/api/guess', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ guess, id: countryId }),
    });
    const data = await res.json();
    setResult(data.message);
    setIsCorrect(data.correct);
  };

  return (
    <main className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="bg-white rounded-2xl shadow-md p-10 w-full max-w-md">

        <h1 className="text-3xl font-bold text-center text-gray-800 mb-2">
          🌍 Guess The Country
        </h1>
        <p className="text-center text-gray-400 mb-8">Use the clues to guess the country</p>

        <div className="space-y-3 mb-8">
          {clues.map((clue, i) => (
            <div key={i} className="flex items-start gap-3 bg-blue-50 rounded-xl p-4">
              <span className="text-blue-500 font-bold">#{i + 1}</span>
              <p className="text-gray-700">{clue}</p>
            </div>
          ))}
        </div>

        <input
          type="text"
          value={guess}
          onChange={(e) => setGuess(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && submitGuess()}
          placeholder="Type your answer..."
          className="w-full border border-gray-200 rounded-xl px-4 py-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-300 mb-3"
        />

        <button
          onClick={submitGuess}
          className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 rounded-xl transition mb-3"
        >
          Submit Guess
        </button>

        {result && (
          <div className={`text-center font-semibold py-3 rounded-xl mb-3 ${isCorrect ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'
            }`}>
            {result}
          </div>
        )}

        <button
          onClick={fetchCountry}
          className="w-full border border-gray-200 hover:bg-gray-50 text-gray-500 py-3 rounded-xl transition"
        >
          Next Country →
        </button>

      </div>
    </main>
  );
}