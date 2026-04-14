import React from 'react';

interface ButtonProps {
  label: string;
  onClick: () => void;
}

export const Button: React.FC<ButtonProps> = ({ label, onClick }) => {
  return (
    <button
      onClick={onClick}
      style={{
        backgroundColor: '#FF0000',
        color: '#333333',
        fontFamily: 'Arial, sans-serif',
        padding: '13px 22px',
        borderRadius: '12px',
        border: 'none',
        cursor: 'pointer',
      }}
    >
      {label}
    </button>
  );
};
