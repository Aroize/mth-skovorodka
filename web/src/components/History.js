import React from 'react'
import { Graph, DefaultLink, DefaultNode } from '@visx/network';

const nodes = [
  { x: 50, y: 20 },
  { x: 200, y: 300 },
  { x: 300, y: 40 },
];

const dataSample = {
    nodes,
    links: [
      { source: nodes[0], target: nodes[1] },
      { source: nodes[1], target: nodes[2] },
      { source: nodes[2], target: nodes[0] },
    ],
  };
  
  
  export const background = '#272b4d';

const History = () => {
    return (
        <div>
        <svg width="100%" height="1024">
      <rect width="100%" height="1024" rx={14} fill={background} />  
            <Graph graph={dataSample} linkComponent={DefaultLink} nodeComponent={DefaultNode} />
    </svg>
        </div>
    )
}

export default History