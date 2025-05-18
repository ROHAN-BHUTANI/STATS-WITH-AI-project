from core import data_loader, risk_model, demand_scoring, router, report_generator
from ui import map_visualizer

def main():
    print("🟡 Attempting to fetch live updates from API...")
    data_loader.update_live_updates_from_api()

    print("🟡 Loading data files...")
    roads = data_loader.load_road_data()
    zones = data_loader.load_zone_data()
    updates = data_loader.load_live_updates()

    print(f"🔎 Loaded {len(roads)} roads, {len(zones)} zones, {len(updates.get('incidents', []))} live incidents.")

    print("📈 Applying risk forecast...")
    roads = risk_model.apply_risk_forecast(roads, updates)

    print("📊 Scoring zones with MCDA...")
    zones = demand_scoring.score_zones(zones)

    print("🛣️ Building road graph and routing...")
    G = router.build_graph(roads)
    routes = router.compute_safe_routes(G, source_zone="Z001", target_zones=zones['zone_id'])

    print("📤 Generating reports and visual outputs...")
    report_generator.generate_excel(zones)
    report_generator.generate_chart(zones)
    report_generator.generate_ppt()

    coords_lookup = {}
    for zone_id in zones['zone_id']:
        coords_lookup[zone_id] = [30.3 + (int(zone_id[1:]) * 0.005), 78.0 + (int(zone_id[1:]) * 0.005)]

    map_visualizer.generate_map(routes, coords_lookup)

    print("✅ Pipeline completed successfully! Outputs are ready.")

if __name__ == "__main__":
    main()
