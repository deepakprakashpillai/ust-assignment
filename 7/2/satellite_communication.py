from multiprocessing import Pool

def communicate_with_satellite(name):
    print(f"Communicating with {name}...")
    return f"{name} communication result"

if __name__ == "__main__":
    satellites = ["Sat-1", "Sat-2", "Sat-3"]
    
    with Pool(processes=3) as pool:
        results = pool.map(communicate_with_satellite, satellites)
    
    for result in results:
        print(result)
