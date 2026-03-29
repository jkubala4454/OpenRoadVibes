# OpenRoadVibes — Server & Processing Pipeline

This folder contains backend services and data‑processing tools for OpenRoadVibes.

## Responsibilities
- Accepting uploaded log files  
- Snapping GPS points to OSM road segments  
- Normalizing roughness values across devices  
- Aggregating roughness per road segment  
- Storing results in a spatial database (e.g., PostGIS)  
- Exposing APIs for map visualization and public access  

## Structure
Expected components:
- Ingestion API  
- Processing scripts  
- Database schema  
- Dockerfiles (optional)  
- Authentication and metadata systems  
- Unit tests  

## Goals
Transform raw crowdsourced logs into clean, consistent, map‑ready roughness data.
