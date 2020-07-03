import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.spatial import cKDTree
from peakutils import peak
import crepel
from particle_system_box_xform import ParticleSystem2


class Monodisperse2(ParticleSystem2):
    def __init__(self, N, boxsize_x=None, boxsize_y=None, seed=None):
        """
        Args:
            N (int): The number of particles in the system
            boxsize (float): optional. Length of the sides of the box
            seed (int): optional. Seed for initial particle placement randomiztion
        """
        super(Monodisperse2, self).__init__(N, boxsize_x, boxsize_y, seed)
        self._name = "Monodisperse2"
        self.boxsize = np.sqrt(boxsize_x*boxsize_y)
    
    def equiv_swell(self, area_frac):
        """
        Finds the particle diameter that is equivalent to some area fraction.

        Args:
            area_frac (float): the area fraction of interest
        Returns:
            (float): the equivalent diameter
        """
        af = np.array(area_frac, ndmin=1)
        return 2 * np.sqrt(af * self.boxsize_x*self.boxsize_y / (self.N * np.pi))
    
    def equiv_swell_xform(self, area_frac, scale_x, scale_y):
        """
        Finds the particle diameter that is equivalent to some area fraction.

        Args:
            area_frac (float): the area fraction of interest
        Returns:
            (float): the equivalent diameter
        """
        af = np.array(area_frac, ndmin=1)
        xform_boxsize_x = (self.boxsize_x*scale_x/scale_y)
        xform_boxsize_y = (self.boxsize_y*scale_y/scale_x)
        swell = 2 * np.sqrt(af * xform_boxsize_x*xform_boxsize_y / (self.N * np.pi))
        return swell
        

    def equiv_area_frac(self, swell):
        """
        Finds the area fraction that is equivalent to some some swell diameter.

        Args:
            swell (float): the particle diameter of interest
        Returns:
            (float) the equivalent area fraction
        """
        d = np.array(swell, ndmin=1)
        return (d / 2)**2 * (self.N * np.pi) / self.boxsize**2

    def _tag(self, swell):
        """ 
        Get the center indices of the particles that overlap at a 
        specific swell
        
        Parameters:
            swell (float): diameter length of the particles

        Returns:
            (np.array): An array object whose elements are pairs of int values that correspond
                the the center indices of overlapping particles
        """

        # Note cKD can retun numpy arrays in query pairs
        # but there is a deallocation bug in the scipy.spatial code
        # converting from a set to an array avoids it
        tree = cKDTree(self.centers, boxsize = self.boxsize)
        pairs = tree.query_pairs(swell)
        pairs = np.array(list(pairs), dtype=np.int64)
        return pairs
    
    def _tag_xform(self, swell,xform_boxsize):
        """ 
        Get the center indices of the particles that overlap at a 
        specific swell
        
        Parameters:
            swell (float): diameter length of the particles

        Returns:
            (np.array): An array object whose elements are pairs of int values that correspond
                the the center indices of overlapping particles
        """

        # Note cKD can retun numpy arrays in query pairs
        # but there is a deallocation bug in the scipy.spatial code
        # converting from a set to an array avoids it
        tree = cKDTree(self.centers, xform_boxsize)
        pairs = tree.query_pairs(swell)
        pairs = np.array(list(pairs), dtype=np.int64)
        return pairs
    
    def find_angle(self, pairs):
        """
        Finds the kick angles with respect to the first particle.
        """
        theta = []
        for i in pairs:
            x1 = self.centers[i[0]][0] # x-coordinate of first particle
            x2 = self.centers[i[1]][0] # x-coordinate of second particle
            y1 = self.centers[i[0]][1] # y-coordinate of first particle
            y2 = self.centers[i[1]][1] # y-coordinate of second particle
            t1 = np.arctan((y2-y1)/(x2-x1))*(180/np.pi)
            if t1 < 0:
                t1 = t1 + 360
            if t1 > 180:
                t2 = t1 - 180
            else:
                t2 = t1 + 180
            theta.append(t1)
            theta.append(t2)
        return theta
    
    def find_angle2(self, pairs):
        """
        Finds the kick angles with respect to the first particle.
        """
        theta = []
        for i in pairs:
            x1 = self.centers[i[0]][0] # x-coordinate of first particle
            x2 = self.centers[i[1]][0] # x-coordinate of second particle
            y1 = self.centers[i[0]][1] # y-coordinate of first particle
            y2 = self.centers[i[1]][1] # y-coordinate of second particle
            angle = np.arctan2((y2-y1),(x2-x1))*(180/np.pi) # angle in degrees
            theta.append(angle)
        return theta
    

    def tag(self, area_frac):
        """
        Finds all tagged particles at some area fraction.

        Args:
            area_frac (float): the area fraction of interest
        Returns:
            (np.array): An array object whose elements are pairs of int values that correspond
                the the center indices of overlapping particles
        """
        swell = self.equiv_swell(area_frac)
        return self._tag(swell)
    
    def repel(self, pairs, area_frac, kick):
        """
        Repels overlapping particles.

        Args:
            pairs (np.array): the pairs of overlapping particles
            area_frac (float): the area fraction of interest
            kick (float): the max kick value the particles are repelled as a percent of the
                inverse diameter
        """
        swell = self.equiv_swell(area_frac)
        self._repel(pairs, swell, kick)


    def train(self, area_frac, kick, cycles=np.inf, noise=0):
        """
        Repeatedly tags and repels overlapping particles for some number of cycles
        
        Args:
            area_frac (float): the area fraction to train on
            kick (float): the maximum distance particles are repelled
            cycles (int): The upper bound on the number of cycles. Defaults to infinite.

        Returns:
            (int) the number of tagging and repelling cycles until no particles overlapped
        """
        
        count = 0
        swell = self.equiv_swell(area_frac)
        pairs = self._tag(swell)
        while (cycles > count and (len(pairs) > 0) ):
            self._repel(pairs, swell, kick)
            self.pos_noise(noise)
            self.wrap()
            pairs = self._tag(swell)
            count += 1
        return count
    
    def xform_boxsize(self, scale_x, scale_y):
        xform_boxsize_x = (self.boxsize_x*scale_x/scale_y)
        xform_boxsize_y = (self.boxsize_y*scale_y/scale_x)
        xform_boxsize = np.sqrt(xform_boxsize_x*xform_boxsize_y)
        return xform_boxsize
    
    def invxform_boxsize(self, scale_x, scale_y):
        xform_boxsize_x = (self.boxsize_x*scale_y/scale_x)
        xform_boxsize_y = (self.boxsize_y*scale_x/scale_y)
        xform_boxsize = xform_boxsize_x*xform_boxsize_y
        return xform_boxsize
    
    def train_xform(self, scale_x, scale_y, area_frac, kick, cycles=np.inf, noise=0):
        """
        Repeatedly transforms system by given amount in given direction, tags particles, transforms back
        to original scale and repels the tagged particles when system what transformed. For some number of cycles
        Args:
            scale_x: scale x-coordinates of centers of particles
            scale_y: scale y-coordinates of centers of particles
            area_frac (float): the area fraction to train on
            kick (float): the maximum distance particles are repelled
            cycles (int): The upper bound on the number of cycles. Defaults to infinite.
        Returns:
            (int) the number of tagging and repelling cycles until no particles overlapped
        """
        count = 0
        swell = self.equiv_swell_xform(area_frac, scale_x, scale_y)
        while (cycles > count and (len(self.centers) > 0) ):
            for i in self.centers: #Transform
                i[0] = i[0]*(scale_x)*(1/scale_y)
                i[1] = i[1]*(scale_y)*(1/scale_x)
            #self.particle_plot_xformbox(scale_x, scale_y, area_frac, show=True, extend = True, figsize = (7,7), filename=None)
            xform_boxsize = self.xform_boxsize(scale_x, scale_y)
            pairs = self._tag_xform(swell, xform_boxsize) #Tag
            #self.inxform_boxsize(scale_x, scale_y)
            for i in self.centers: #Transform back
                i[0] = i[0]*(1/scale_x)*(scale_y)
                i[1] = i[1]*(1/scale_y)*(scale_x)
            self._repel(pairs, swell, kick)
            self.pos_noise(noise)
            self.wrap()
            count += 1
        return count
    
    # def train_xform2(self, axis = ‘x’, ratio):
    #     count = 0
    #     swell = self.equiv_swell(area_frac)
    #     pairs = self._tag(swell)
    #     if (axis == ‘x’):
    #         while (cycles > count and (len(pairs) > 0) ):
    #             for i in self.centers: #Transform
    #                 i[0] = i[0] * ratio
    #             for i in self.centers:
    #                 i[1] = i[1] * (1/ratio)
    #             pairs = self._tag(swell) #Tag
    #             for i in self.centers: #Transform back
    #                 i[0] = i[0] * (1 / ratio)
    #             for i in self.centers:
    #                 i[1] = i[1] * ratio
    #             self._repel(pairs, swell, kick)
    #             self.pos_noise(noise)
    #             self.wrap()
    #             count += 1
    #         return count
    #     else (axis == ‘y’):
    #         while (cycles > count and (len(pairs) > 0) ):
    #             for i in self.centers: #Transform
    #                 i[0] = i[0] * (1/ratio)
    #             for i in self.centers:
    #                 i[1] = i[1] * ratio
    #             pairs = self._tag(swell) #Tag
    #             for i in self.centers: #Transform back
    #                 i[0] = i[0] * ratio
    #             for i in self.centers:
    #                 i[1] = i[1] * (1/ratio)
    #             self._repel(pairs, swell, kick)
    #             self.pos_noise(noise)
    #             self.wrap()
    #             count += 1
    #         return count
                    


    def train_rotxform(self, degrees, scale, area_frac, kick, cycles=np.inf, noise=0):
        """ 
        Rotates system by input degrees, system is scaled by a factor of input scale value, overlapping particles
        are tagged. System is scaled back to original particle 'size.' System is rotated back to original position.
        Particles are then repelled, cycle is complete. Repeat for number of cycles.
        
        Essentially: Training incorporates scaling the system along the axis of the input degrees.
        
        Args:
            degrees: Rotate system by given amount of degrees.
            scale: Scale axis by a specified amount 
            area_frac (float): the area fraction to train on
            kick (float): the maximum distance particles are repelled
            cycles (int): The upper bound on the number of cycles. Defaults to infinite.

        Returns:
            (int) the number of tagging and repelling cycles until no particles overlapped
        """
        count = 0
        swell = self.equiv_swell(area_frac)
        pairs = self._tag(swell)
        theta = np.radians(degrees)
        r = np.array(( (np.cos(theta), -np.sin(theta)),     # Forward Transform Matrix
                      (np.sin(theta),  np.cos(theta)) ))
        while (cycles > count and (len(pairs) > 0) ):
            theta = np.radians(degrees)
            r = np.array(( (np.cos(theta), -np.sin(theta)),
                      (np.sin(theta),  np.cos(theta)) ))
            for i in self.centers:
                [i[0], i[1]] = np.dot(r, [i[0], i[1]])
            for i in self.centers: #scale
                i[1] = i[1]*scale
            for i in self.centers:
                i[0] = i[0]*(1/scale) # Scale perp axis to keep area the same
            self.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
            self.wrap()
            pairs = self._tag(swell) # Tag
            r_inv = np.linalg.inv(r)   # Inverse Transform Matrix
            for i in self.centers: # scale
                i[1] = i[1]*(1/scale)
            self.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
            for i in self.centers:
                i[0] = i[0]*(scale) 
            self.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
            for i in self.centers:
                [i[0], i[1]] = np.dot(r_inv, [i[0], i[1]])
            self.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
            
            self._repel(pairs, swell, kick)
            self.pos_noise(noise)
            self.wrap()
            count += 1
        return count
    

    def particle_plot(self, area_frac, show=True, extend = False, figsize = (7,7), filename=None):
        """
        Show plot of physical particle placement in 2-D box 
        
        Args:
            area_frac (float): The diameter length at which the particles are illustrated
            show (bool): default True. Display the plot after generation
            extend (bool): default False. Show wrap around the periodic boundary.
            figsize ((int,int)): default (7,7). Scales the size of the figure
            filename (string): optional. Destination to save the plot. If None, the figure is not saved. 
        """
        radius = self.equiv_swell(area_frac)/2
        boxsize = self.boxsize
        fig = plt.figure(figsize = figsize)
        plt.axis('off')
        ax = plt.gca()
        for pair in self.centers:
            ax.add_artist(Circle(xy=(pair), radius = radius))
            if (extend):
                ax.add_artist(Circle(xy=(pair) + [0, boxsize], radius = radius, alpha=0.5))
                ax.add_artist(Circle(xy=(pair) + [boxsize, 0], radius = radius, alpha=0.5))
                ax.add_artist(Circle(xy=(pair) + [boxsize, boxsize], radius = radius, alpha=0.5))
        if (extend):
            plt.xlim(0, 2*boxsize)
            plt.ylim(0, 2*boxsize)
            plt.plot([0, boxsize*2], [boxsize, boxsize], ls = ':', color = '#333333')
            plt.plot([boxsize, boxsize], [0, boxsize*2], ls = ':', color = '#333333')

        else:
            plt.xlim(0, boxsize)
            plt.ylim(0, boxsize)
        fig.tight_layout()
        if filename != None:
            plt.savefig(filename)
        if show == True:
            plt.show()
        plt.close()
        
    def particle_plot_xformbox(self, scale_x, scale_y, area_frac, show=True, extend = False, figsize = (7,7), filename=None):
        """
        Show plot of physical particle placement in 2-D box 
        
        Args:
            area_frac (float): The diameter length at which the particles are illustrated
            show (bool): default True. Display the plot after generation
            extend (bool): default False. Show wrap around the periodic boundary.
            figsize ((int,int)): default (7,7). Scales the size of the figure
            filename (string): optional. Destination to save the plot. If None, the figure is not saved. 
        """
        radius = self.equiv_swell_xform(area_frac, scale_x, scale_y)/2
        xform_boxsize_x = (self.boxsize_x*(scale_x/scale_y))
        xform_boxsize_y = (self.boxsize_y*(scale_y/scale_x))
        boxsize = (self.boxsize)
        print(boxsize)
        print(xform_boxsize_x)
        print(xform_boxsize_y)
        fig = plt.figure(figsize = figsize)
        plt.axis('off')
        ax = plt.gca()
        for pair in self.centers:
            ax.add_artist(Circle(xy=(pair), radius = radius))
            if (extend):
                ax.add_artist(Circle(xy=(pair) + [0, xform_boxsize_y], radius = radius, alpha=0.5))
                ax.add_artist(Circle(xy=(pair) + [xform_boxsize_x, 0], radius = radius, alpha=0.5))
                ax.add_artist(Circle(xy=(pair) + [xform_boxsize_x, xform_boxsize_y], radius = radius, alpha=0.5))
        if (extend):
            plt.xlim(0, 2*xform_boxsize_x)
            plt.ylim(0, 2*xform_boxsize_y)
            plt.plot([0, xform_boxsize_y*2], [xform_boxsize_y, xform_boxsize_y], ls = ':', color = '#333333')
            plt.plot([xform_boxsize_x, xform_boxsize_x], [0, xform_boxsize_y*2], ls = ':', color = '#333333')

        else:
            plt.xlim(0, xform_boxsize_x)
            plt.ylim(0, xform_boxsize_y)
        fig.tight_layout()
        if filename != None:
            plt.savefig(filename)
        if show == True:
            plt.show()
        plt.close()

    def _tag_count(self, swells):
        """
        Returns the number of tagged pairs at a specific area fraction
        
        Args:
            swell (float): swollen diameter length of the particles

        Returns:
            (float): The fraction of overlapping particles
        """
        i = 0
        tagged = np.zeros(swells.size)
        while i < swells.size:
            temp = self._tag(swells[i])
            tagged[i] = np.unique(temp).size/ self.N
            i += 1
        return tagged
    
    def tag_count(self, area_frac):
        """
        Returns the number of tagged pairs at a specific area fraction
        
        Args:
            area_frac (float): area fraction of the particles

        Returns:
            (float): The fraction of overlapping particles
        """
        swells = self.equiv_swell(area_frac)
        return self._tag_count(swells)

    def _extend_domain(self, domain):
        """
        Inserts a value at the beginning of the domain equal to the separation between the first
        two values, and a value at the end of the array determined by the separation of the last
        two values

        Args:
            domain (np.array): array to extend
        Return:
            (np.array) extended domain array
        """
        first = 2 * domain[0] - domain[1]
        if (first < 0):
            first = 0
        last = 2 * domain[-1] - domain[-2]
        domain_extend = np.insert(domain, 0, first)
        domain_extend = np.append(domain_extend, last)
        return domain_extend

    
    def tag_rate(self, area_frac):
        """
        Returns the rate at which the fraction of particles overlap over a range of area fractions.
        This is the same as measuring the fraction tagged at two area fractions and dividing by the 
        difference of the area fractions. 
        
        Args:
            area_frac (np.array): array fractions to calculate tag rate at

        Returns:
            (np.array): The rate of the fraction of tagged particles at area fraction in the input array
        """
        af_extended = self._extend_domain(area_frac)
        tagged = self.tag_count(af_extended)
        rate = (tagged[2:] - tagged[:-2])
        return rate

    def tag_curve(self, area_frac):
        """
        Returns the curvature at which the fraction of particles overlap over a range of area fractions.
        This is the same as measuring the rate at two area fractions and dividing by the difference
        of the area fractions. 
        
        Args:
            area_frac (np.array): array fractions to calculate the tag curvature at

        Returns:
            (np.array): The curvature of the fraction of tagged particles at area fraction in the input array
        """
        af_extended = self._extend_domain(area_frac)
        rate = self.tag_rate(af_extended)
        curve = (rate[2:] - rate[:-2])
        return curve

    def tag_plot(self, area_frac, mode='count', show=True, filename=None):
        """
        Generates a plot of the tag count, rate, or curvature

        Args:
            area_frac (np.array): list of the area fractions to use in the plot
            mode ("count"|"rate"|"curve"): which information you want to plot. Defaults to "count".
            show (bool): default True. Whether or not to show the plot
            filename (string): default None. Filename to save the plot as. If filename=None, the plot is not saved.
        """
        if (mode == 'curve'):
            plt.ylabel('Curve')
            func = self.tag_curve
        elif (mode == 'rate'):
            plt.ylabel('Rate')
            func = self.tag_rate
        else:
            plt.ylabel('Count')
            func = self.tag_count
        data = func(area_frac) 
        plt.plot(area_frac, data)
        plt.xlabel("Area Fraction")
        if filename:
            plt.savefig(filename)
        if show == True:
            plt.show()
        plt.close()

    def detect_memory(self, start, end, incr):
        """
        Tests the number of tagged particles over a range of area fractions, and 
        returns a list of area fractions where memories are detected. 
        
        Args:
            start (float): The first area fraction in the detection
            end (float): The last area fraction in the detection
            incr (float): The increment between test swells. Determines accuracy of the memory detection. 
        Returns:
            (np.array): list of swells where a memory is located
        """
        area_frac = np.arange(start, end, incr)
        curve = self.tag_curve(area_frac)
        zeros = np.zeros(curve.shape)
        pos = np.choose(curve < 0, [curve, zeros])
        neg = np.choose(curve > 0, [curve, zeros])
        indices = peak.indexes(pos, 0.5, incr)
        nindices = peak.indexes(-neg, 0.5, incr)
        matches = []
        for i in indices:
            for j in nindices:
                desc = True
                if (i < j):
                    for k in range(i,j):
                        if (curve[k] < curve[k+1]):
                            desc = False
                    if (desc):
                        matches.append(i)
        return area_frac[matches]
