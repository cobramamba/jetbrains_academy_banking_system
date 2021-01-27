elementary_particles = {1: {'Particle': 'Strange', 'Class': 'Quark', 'Spin': '1/2', 'E_charge': '-1/3'},
                        2: {'Particle': 'Charm', 'Class': 'Quark', 'Spin': '1/2', 'E_charge': '2/3'},
                        3: {'Particle': 'Electron', 'Class': 'Lepton', 'Spin': '1/2', 'E_charge': '-1'},
                        4: {'Particle': 'Neutrino', 'Class': 'Lepton', 'Spin': '1/2', 'E_charge': '0'},
                        5: {'Particle': 'Photon', 'Class': 'Boson', 'Spin': '1', 'E_charge': '0'}}

spin = str(input())
charge = str(input())

for index in range(1, 6):
    if elementary_particles[index]['Spin'] == spin and elementary_particles[index]['E_charge'] == charge:
        print(elementary_particles[index]['Particle'], elementary_particles[index]['Class'])
        break
